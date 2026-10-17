"""
poll_results.py
===============
1. Polls pending jobs and marks "completed": True in jobs.json when finished.
2. When all pages for a PDF are completed, fetches their responses sequentially
   in page order (1..N), writes extract/to/{pdf_name}.md, and cleans up jobs.json.

Usage:
    python extract/poll_results.py         # Loop until all PDFs are written
    python extract/poll_results.py --once  # Single sweep
"""

import argparse
import json
import logging
import sys
import time
from collections import defaultdict
from pathlib import Path

import httpx

GATEWAY = "http://localhost:8000"
JOBS_FILE = Path("extract/jobs.json")
TO_DIR = Path("extract/to")
POLL_INTERVAL = 3

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stderr,
    format="%(asctime)s  %(levelname)-7s  %(message)s",
)
logger = logging.getLogger(__name__)


def load_jobs() -> list[dict]:
    if not JOBS_FILE.exists():
        return []
    try:
        return json.loads(JOBS_FILE.read_text())
    except Exception:
        return []


def save_jobs(jobs: list[dict]) -> None:
    JOBS_FILE.parent.mkdir(parents=True, exist_ok=True)
    JOBS_FILE.write_text(json.dumps(jobs, indent=2))


def fetch_job(client: httpx.Client, job_id: str) -> dict:
    r = client.get(f"{GATEWAY}/{job_id}", timeout=15)
    r.raise_for_status()
    return r.json()


def write_assembled_pdf(client: httpx.Client, pdf_name: str, pdf_jobs: list[dict]) -> None:
    """Fetch each page sequentially in page order and write the Markdown file."""
    pdf_jobs_sorted = sorted(pdf_jobs, key=lambda j: j["page_num"])
    logger.info(f"All pages ready for '{pdf_name}'. Fetching sequentially in order...")

    TO_DIR.mkdir(parents=True, exist_ok=True)
    out_path = TO_DIR / f"{pdf_name}.md"

    with open(out_path, "w", encoding="utf-8") as f:
        for job in pdf_jobs_sorted:
            page_num = job["page_num"]
            data = fetch_job(client, job["job_id"])
            status = data.get("status")
            response_text = data.get("response") or ""

            if status == "failed":
                response_text = f"<!-- EXTRACTION FAILED FOR PAGE {page_num} -->\n{response_text}"

            f.write(f"\n## Page {page_num}\n\n{response_text}\n")
            logger.info(f"  fetched & written {pdf_name} page {page_num}")

    logger.info(f"Successfully assembled → {out_path} ({len(pdf_jobs_sorted)} pages)")


def run_poll(once: bool) -> None:
    with httpx.Client() as client:
        while True:
            jobs = load_jobs()
            if not jobs:
                logger.info("No jobs remaining in jobs.json.")
                break

            changed = False

            # 1. Poll uncompleted jobs to check status and mark boolean
            for job in jobs:
                if job.get("completed"):
                    continue

                try:
                    res = fetch_job(client, job["job_id"])
                    status = res.get("status")
                    if status in ("completed", "failed"):
                        job["completed"] = True
                        changed = True
                        logger.info(
                            f"Status ready: {job['pdf_name']} page {job['page_num']} ({status})"
                        )
                except Exception as exc:
                    logger.warning(f"Error checking {job['job_id']}: {exc}")

            # 2. Check if all parts for any PDF are completed
            by_pdf = defaultdict(list)
            for job in jobs:
                by_pdf[job["pdf_name"]].append(job)

            finished_pdfs = set()
            for pdf_name, pdf_jobs in by_pdf.items():
                if all(j.get("completed") for j in pdf_jobs):
                    write_assembled_pdf(client, pdf_name, pdf_jobs)
                    finished_pdfs.add(pdf_name)

            # 3. Clean up finished PDFs from jobs.json
            if finished_pdfs:
                jobs = [j for j in jobs if j["pdf_name"] not in finished_pdfs]
                changed = True

            if changed:
                save_jobs(jobs)

            pending = sum(1 for j in jobs if not j.get("completed"))
            if once or not jobs:
                logger.info(
                    f"Sweep complete. Remaining pending pages: {pending}, Active PDFs: {len(by_pdf) - len(finished_pdfs)}"
                )
                break

            time.sleep(POLL_INTERVAL)


def main() -> None:
    parser = argparse.ArgumentParser(description="Poll async jobs and assemble Markdown.")
    parser.add_argument(
        "--once",
        action="store_true",
        help="Do a single sweep and exit instead of looping.",
    )
    args = parser.parse_args()
    run_poll(once=args.once)


if __name__ == "__main__":
    main()
