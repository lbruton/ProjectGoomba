# ProjectGoombaStomp CLI (`goomba`)

ProjectGoombaStomp is a **one‑shot documentation sweeper**: point it at a directory and it spits out a tidy Markdown digest of the folder tree *plus* the text‑friendly contents of every relevant file.  
Optionally, it can:

* package the result into a UTF‑8‑safe PDF,
* bundle everything into a ZIP archive,
* include source‑code files in the output with a single switch.

Perfect for quick code audits, compliance snapshots, or handing projects over to teammates.

---

## 📦 Installation

### 1. Local‑user one‑liner *(recommended)*

```bash
# download & unpack the release archive
unzip projectgoomba_v1.0.4.zip
cd projectgoomba_v1.0.4

# run the helper
chmod +x install.sh
./install.sh
```

`install.sh` does three things:

1. `pip install --user .` – installs the Python package in your user site‑packages;
2. figures out where `pip` actually dropped the launcher (macOS puts it in `~/Library/Python/<ver>/bin`);
3. symlinks that launcher to **`~/.local/bin/goomba`**.

Make sure `~/.local/bin` is on your `PATH` (add `export PATH="$HOME/.local/bin:$PATH"` to your shell profile if needed).

### 2. Plain pip

```bash
pip install --user projectgoombastomp==1.0.4
```

(You’ll still need to add the user‑bin directory to your `PATH`.)

### 3. Developer/editable install

```bash
git clone https://github.com/yourhandle/ProjectGoombaStomp.git
pip install --user -e ProjectGoombaStomp
```

---

## 🔧 Usage

```bash
goomba /path/to/folder [OPTIONS]
```

| Flag | Description |
|------|-------------|
| `--include-code` | Also pull in `.py`, `.js`, `.html`, `.css` files. |
| `--pdf` | Render the markdown to **merged_output.pdf** (UTF‑8 aware via Arial Unicode). |
| `--zip` | Bundle every generated artefact into **merged_output.zip**. |

> **Output location:** everything is written to a new `merged/` sub‑folder inside the target directory, using the base name `merged_output` plus the extension(s) you requested.

### Examples

Generate a Markdown inventory only:

```bash
goomba ./my_project
```

Generate Markdown + PDF, pulling in code files as well:

```bash
goomba ./my_project --include-code --pdf
```

Full boat (Markdown, PDF, ZIP):

```bash
goomba ./my_project --include-code --pdf --zip
```

---

## 🧽 Uninstall

From the extracted release folder:

```bash
chmod +x uninstall.sh
./uninstall.sh
```

The script removes the launcher symlink, uninstalls the pip package, and cleans up `~/.goombastomp` cache (if you created one).

---



