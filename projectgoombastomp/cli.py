import os
import argparse
from fpdf import FPDF
import os
import zipfile

def build_folder_structure(root_dir):
    structure_lines = []
    def recurse(current_path, prefix=""):
        entries = sorted(
            e for e in os.listdir(current_path)
            if not e.startswith('.') and not e.startswith('._') and e not in {'node_modules', '.git'}
        )
        for i, entry in enumerate(entries):
            path = os.path.join(current_path, entry)
            connector = "└── " if i == len(entries) - 1 else "├── "
            structure_lines.append(f"{prefix}{connector}{entry}")
            if os.path.isdir(path):
                extension = "    " if i == len(entries) - 1 else "│   "
                recurse(path, prefix + extension)
    structure_lines.append(os.path.basename(root_dir.rstrip("/")) + "/")
    recurse(root_dir)
    return "\n".join(structure_lines)

def collect_file_contents(root_dir, valid_exts):
    contents = []
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if not d.startswith('.') and not d.startswith('._') and d not in {'node_modules', '.git'}]
        for file in sorted(files):
            if file.startswith('.') or file.startswith('._'):
                continue
            if any(file.lower().endswith(ext) for ext in valid_exts):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, root_dir)
                try:
                    with open(full_path, 'r', encoding='utf-8') as f:
                        data = f.read()
                except Exception as e:
                    data = f"[ERROR reading file: {e}]"
                contents.append(f"\n\n### {rel_path}\n```\n{data}\n```")
    return "\n".join(contents)

def generate_markdown(root_dir, valid_exts):
    structure = build_folder_structure(root_dir)
    content = collect_file_contents(root_dir, valid_exts)
    return f"# Folder Structure\n\n```\n{structure}\n```\n\n# File Contents\n{content}"

def save_markdown(content, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

def save_pdf(content, output_path):
    # Bundle and load ArialUnicode font
    font_dir = os.path.join(os.path.dirname(__file__), 'fpdf_fonts')
    font_path = os.path.join(font_dir, 'ArialUnicode.ttf')
    pdf = FPDF()
    # Load ArialUnicode font after PDF init
    font_dir = os.path.join(os.path.dirname(__file__), 'fpdf_fonts')
    font_path = os.path.join(font_dir, 'ArialUnicode.ttf')
    pdf.add_font('ArialUnicode', '', font_path, uni=True)
    pdf.set_auto_page_break(auto=True, margin=10)
    pdf.add_page()

    font_path = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
    if not os.path.exists(font_path):
        raise RuntimeError("Font not found. Please update font_path to a valid Unicode TTF.")

    pdf.add_font("ArialUnicode", fname=font_path, uni=True)

    for line in content.splitlines():
        while len(line) > 95:
            pdf.cell(0, 5, line[:95], ln=True)
            line = line[95:]
        pdf.cell(0, 5, line, ln=True)

    pdf.output(output_path)

def save_zip(files_to_zip, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in files_to_zip:
            zipf.write(file, os.path.basename(file))

def main():
    parser = argparse.ArgumentParser(description="Merge folder to Markdown with optional PDF/ZIP export (UTF-8 safe)")
    parser.add_argument("folder", help="Path to folder")
    parser.add_argument("--include-code", action="store_true", help="Include .py, .js, .html, .css")
    parser.add_argument("--pdf", action="store_true", help="Export as PDF")
    parser.add_argument("--zip", action="store_true", help="Create ZIP archive")

    args = parser.parse_args()
    base_path = os.path.abspath(args.folder)
    merged_dir = os.path.join(base_path, "merged")
    os.makedirs(merged_dir, exist_ok=True)
    base_output = os.path.join(merged_dir, "merged_output")
    valid_exts = {".txt", ".md", ".log", ".csv", ".json", ".xml", ".yaml", ".yml", ".ini"}

    if args.include_code:
        valid_exts |= {".py", ".html", ".js", ".css"}

    markdown = generate_markdown(base_path, valid_exts)
    files_created = []

    md_path = base_output + ".md"
    save_markdown(markdown, md_path)
    files_created.append(md_path)

    if args.pdf:
        pdf_path = base_output + ".pdf"
        save_pdf(markdown, pdf_path)
        files_created.append(pdf_path)

    if args.zip:
        zip_path = base_output + ".zip"
        save_zip(files_created, zip_path)
        print(f"✅ Created ZIP: {zip_path}")

    print("✅ Done. Files created:")
    for f in files_created:
        print(f" - {f}")
