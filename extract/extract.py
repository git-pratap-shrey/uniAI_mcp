import pymupdf
import ollama

doc = pymupdf.open("file.pdf")

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

with open("output.md", "w", encoding="utf-8") as f:
    f.write(text)