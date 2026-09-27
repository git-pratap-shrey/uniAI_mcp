from mcp.server import MCPServer
import logging, sys, json
from mcp.server.transport_security import TransportSecuritySettings
from .loads import load_syllabus, get_syllabus_path

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stderr,
)

logger = logging.getLogger(__name__)
mcp = MCPServer("uniAI")


with open("src/uniAI_mcp/availability.json", "r") as file:
    availability = json.load(file)
    

def is_supported(university: str, year: int, subject: str) -> bool:
    if availability.get("university") != university:
        return False

    semesters = availability.get("year", {}).get(str(year), {}).get("semester", {})
    all_subjects = [
        s for sem_data in semesters.values() for s in sem_data.get("subjects", [])
    ]
    return subject in all_subjects


@mcp.tool()
def get_syllabus(university: str, year: int, subject: str) -> str:
    """
    Fetch the syllabus content for a subject. Checks availability first.
    """

    if not is_supported(university, year, subject):
        return f"ERROR: No syllabus available for {university}, year {year}, {subject}. check the availability first."

    path = get_syllabus_path(university, year, subject)
    if not path.exists():
        return f"ERROR: Syllabus file missing on disk for {university}, year {year}, {subject}."
    
    return load_syllabus(university, year, subject)


@mcp.tool()
def get_availability() -> str:

    """
        Lists the academic content currently supported by this MCP server.
        Check this resource before attempting to access university-specific
        study material.
    """

    return json.dumps(availability, indent=4)




@mcp.prompt()
def uniAI_instructions() -> str:
    return """
You are using the uniAI MCP server.

Purpose:
- Provide university study material.
- This includes subject-wise and unit-wise notes, previous year questions and current academic syllabus.

Before searching for academic material:
1. Read `info://availability`.
2. Verify that the requested university, year,
   semester, and subject are supported. If unsure, Ask the user for confirmation before proceeding.
3. Only then use the available search tools.

Do not claim that material is available if it is not
listed in `get_availability` tool.
"""

if __name__ == "__main__":
    security = TransportSecuritySettings(
        allowed_hosts=[
            "uniai-mcp.git-pratap-shrey.online",
            "uniai-mcp.git-pratap-shrey.online:*",
        ],
    )

    mcp.run(
        transport="streamable-http",
        port=3001,
        transport_security=security,
    )