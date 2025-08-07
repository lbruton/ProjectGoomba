
import os
import argparse
import zipfile
from fpdf import FPDF


# ─── Helpers ────────────────────────────────────────────────────────────────────
def build_folder_structure(root_dir: str) -> str:
    """Return a tree-view of the folder, excluding hidden and large junk dirs."""
    lines = []

    def walk(path: str, prefix: str = ""):
        entries = sorted(
            e
            for e in os.listdir(path)
            if not e.startswith((".", "._")) and e not in {"node_modules", ".git"}
        )
        for i, name in enumerate(entries):
            full = os.path.join(path, name)
            connector = "└── " if i == len(entries) - 1 else "├── "
            lines.append(f"{prefix}{connector}{name}")
            if os.path.isdir(full):
                walk(full, prefix + ("    " if i == len(entries) - 1 else "│   "))

    lines.append(os.path.basename(root_dir.rstrip("/")) + "/")
    walk(root_dir)
    return "\n".join(lines)


def collect_file_contents(root_dir: str, exts: set[str]) -> str:
    """Read all matching files and return one big Markdown section."""
    parts = []
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if not d.startswith((".", "._")) and d not in {".git"}]
        for file in sorted(files):
            if file.startswith((".", "._")) or not any(file.lower().endswith(e) for e in exts):
                continue
            rel = os.path.relpath(os.path.join(root, file), root_dir)
            try:
                with open(os.path.join(root, file), encoding="utf-8") as fh:
                    data = fh.read()
            except Exception as e:
                data = f"[ERROR reading file: {e}]"
            parts.append(f"\n\n### {rel}\n```text\n{data}\n```")

    return "\n".join(parts)


def generate_markdown(root_dir: str, exts: set[str]) -> str:
    return (
        "# Folder Structure\n\n```\n"
        + build_folder_structure(root_dir)
        + "\n```\n\n# File Contents\n"
        + collect_file_contents(root_dir, exts)
    )


# ─── Export helpers ─────────────────────────────────────────────────────────────
def save_markdown(md: str, out: str):
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(md)


def save_pdf(md: str, out: str):
    font_dir = os.path.join(os.path.dirname(__file__), "fpdf_fonts")
    font_path = os.path.join(font_dir, "NotoSans-Regular.ttf")

    if not os.path.exists(font_path):
        raise RuntimeError(
            f"Bundled font missing at {font_path}. Re-install or rebuild the package."
        )

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=10)
    pdf.add_page()
    pdf.add_font("NotoSans", "", font_path, uni=True)
    pdf.set_font("NotoSans", "", 12)

    for line in md.splitlines():
        while len(line) > 95:
            pdf.cell(0, 5, line[:95], ln=True)
            line = line[95:]
        pdf.cell(0, 5, line, ln=True)

    pdf.output(out)


def save_zip(paths: list[str], out: str):
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in paths:
            z.write(p, os.path.basename(p))


# ─── CLI ────────────────────────────────────────────────────────────────────────
def main():
    p = argparse.ArgumentParser(
        prog="goomba",
        description="Merge a folder into Markdown (plus optional PDF/ZIP) – UTF-8 safe",
    )
    p.add_argument("folder", help="Path to the folder you want to document")
    p.add_argument("--include-code", action="store_true", help="Include code files")
    p.add_argument("--pdf", action="store_true", help="Export a PDF")
    p.add_argument("--zip", action="store_true", help="Bundle outputs into a ZIP")
    args = p.parse_args()

    base = os.path.abspath(args.folder)
    merged_dir = os.path.join(base, "merged")
    os.makedirs(merged_dir, exist_ok=True)

    out_base = os.path.join(merged_dir, "merged_output")
    exts = {".txt", ".md", ".log", ".csv", ".json", ".xml", ".yaml", ".yml", ".ini"}
    if args.include_code:
        exts |= {".py", ".html", ".js", ".css"}

    md_path = out_base + ".md"
    save_markdown(generate_markdown(base, exts), md_path)

    created = [md_path]
    if args.pdf:
        pdf_path = out_base + ".pdf"
        save_pdf(open(md_path, encoding="utf-8").read(), pdf_path)
        created.append(pdf_path)
    if args.zip:
        zip_path = out_base + ".zip"
        save_zip(created, zip_path)
        print(f"✅ Created ZIP: {zip_path}")

    print("✅ Done. Files created:")
    for f in created:
        print(f" • {f}")


if __name__ == "__main__":
    main()
