import base64
import json
import logging
import os
import sys
from pathlib import Path

import httpx
import pymupdf

logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger(__name__)

GATEWAY   = "http://localhost:8000"
JOBS_FILE = Path("extract/jobs.json")
FROM_DIR  = Path("extract/from")
TO_DIR    = Path("extract/to")

TO_DIR.mkdir(parents=True, exist_ok=True)
jobs = json.loads(JOBS_FILE.read_text()) if JOBS_FILE.exists() else []

with httpx.Client() as client:
    for filename in sorted(FROM_DIR.iterdir()):
        if filename.suffix.lower() != ".pdf":
            continue
        name = filename.stem

        if (TO_DIR / f"{name}.md").exists():
            logger.info(f"Skipping {name}.pdf — already extracted")
            continue

        doc = pymupdf.open(filename)
        logger.info(f"Submitting {filename.name} ({len(doc)} pages) …")

        for i, page in enumerate(doc, 1):
            pix    = page.get_pixmap()
            b64    = base64.b64encode(pix.tobytes("png")).decode()

            r = client.post(f"{GATEWAY}/api/async", json={
                "provider": "ollama_cloud",
                "model":    "gemma4:cloud",
                "messages": [{
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Extract all text from this page. Return markdown."},
                        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64}"}},
                    ],
                }],
                "parameters": {"temperature": 0},
            }, timeout=15)
            r.raise_for_status()

            job_id = r.json()["job_id"]
            jobs.append({
                "job_id": job_id,
                "pdf_name": name,
                "page_num": i,
                "completed": False,
            })
            JOBS_FILE.write_text(json.dumps(jobs, indent=2))
            logger.info(f"  page {i} → {job_id}")

logger.info(f"Done. {len(jobs)} job(s) in {JOBS_FILE}. Run poll_results.py to collect.")