import pymupdf
import ollama
import os
import logging, sys

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stderr,
)

logger = logging.getLogger(__name__)

for filename in os.listdir("extract/from"):
    if not filename.endswith(".pdf"):
        continue
    name = filename[:-4]
    
    if os.path.exists(f"extract/to/{name}.md"):
        continue

    doc = pymupdf.open(f"extract/from/{name}.pdf")

    logger.info(f"extracting: {name}.pdf: ")

    text = ""

    for i, page in enumerate(doc, 1):
        pix = page.get_pixmap()
        pix.save("/tmp/page.png")

        res = ollama.chat(
            model="gemma4:cloud",
            messages=[{
                "role": "user",
                "content": "Extract all text from this page. return markdown text",
                "images": ["/tmp/page.png"]
            }],
            options={"temperature": 0}
        )

        text += f"\n## Page {i}\n\n{res['message']['content']}\n"

        logger.info(f"Completed Page : {i}")

    with open(f"extract/to/{name}.md", "w", encoding="utf-8") as f:
        f.write(text)

    logger.info(f"completed: {name}.pdf: ")
    