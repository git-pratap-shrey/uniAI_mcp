import os
import glob
import subprocess
import sys
import tempfile
import shutil


def install_deps():
    deps = [
        "pymupdf",
        "einops",
        "addict",
        "easydict",
        "transformers==4.45.2",   # pin: newer versions dropped is_torch_fx_available used by baidu/Unlimited-OCR
        "accelerate",
    ]
    print(f"Installing dependencies: {deps}")
    subprocess.check_call([sys.executable, "-m", "pip", "install"] + deps)


def pdf_to_images(pdf_path, dpi=300):
    """Convert PDF pages to images for the model."""
    import pymupdf as fitz  # use pymupdf directly to avoid deprecation warning
    doc = fitz.open(pdf_path)
    tmp_dir = tempfile.mkdtemp(prefix="pdf_ocr_")
    mat = fitz.Matrix(dpi / 72, dpi / 72)
    paths = []
    for i, page in enumerate(doc):
        out = os.path.join(tmp_dir, f"page_{i+1:04d}.png")
        page.get_pixmap(matrix=mat).save(out)
        paths.append(out)
    doc.close()
    return tmp_dir, paths


def run_ocr():
    import torch
    from transformers import AutoModel, AutoTokenizer

    model_name = "baidu/Unlimited-OCR"

    print(f"Loading {model_name}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

    # Load fully in float32 to avoid Half/Float dtype mismatch in masked_scatter_
    # (the vision encoder emits float32 tensors regardless of torch_dtype)
    model = AutoModel.from_pretrained(
        model_name,
        trust_remote_code=True,
        use_safetensors=True,
        torch_dtype=torch.float32,
    )
    model = model.eval().cuda()

    input_dir = "/kaggle/input/testing/"
    output_dir = "/kaggle/working/"

    if not os.path.exists(input_dir):
        print(f"Input directory {input_dir} not found. Mounted inputs:")
        for p in os.listdir("/kaggle/input/"):
            print(f"  /kaggle/input/{p}")
        return

    pdfs = sorted(f for f in os.listdir(input_dir) if f.endswith(".pdf"))
    print(f"Found {len(pdfs)} PDF(s): {pdfs}")

    for pdf_file in pdfs:
        pdf_path = os.path.join(input_dir, pdf_file)
        stem = pdf_file.replace(".pdf", "")
        md_path = os.path.join(output_dir, stem + ".md")

        if os.path.exists(md_path):
            print(f"Skipping {pdf_file}, already done.")
            continue

        print(f"\nProcessing {pdf_file}...")

        tmp_dir, images = pdf_to_images(pdf_path)

        try:
            per_file_out = os.path.join(output_dir, f"_tmp_{stem}")
            os.makedirs(per_file_out, exist_ok=True)

            model.infer_multi(
                tokenizer,
                prompt="<image>document parsing.",
                image_files=images,
                output_path=per_file_out,
                image_size=1024,
                max_length=32768,
                no_repeat_ngram_size=35,
                ngram_window=1024,
                save_results=True,
            )

            # Collect all .md/.txt output files and merge into one final .md
            result_files = sorted(
                glob.glob(os.path.join(per_file_out, "*.md"))
                + glob.glob(os.path.join(per_file_out, "*.txt"))
            )

            if result_files:
                with open(md_path, "w", encoding="utf-8") as out_f:
                    for rf in result_files:
                        with open(rf, encoding="utf-8") as in_f:
                            out_f.write(in_f.read())
                            out_f.write("\n\n")
                print(f"  -> Saved merged output to {md_path}")
            else:
                all_files = os.listdir(per_file_out)
                print(f"  -> No .md/.txt found. Files in output dir: {all_files}")

            shutil.rmtree(per_file_out, ignore_errors=True)

        finally:
            shutil.rmtree(tmp_dir, ignore_errors=True)

    print("\nAll done.")


if __name__ == "__main__":
    install_deps()
    run_ocr()
