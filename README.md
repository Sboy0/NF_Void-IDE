# 🚀 NF_Void IDE

A lightweight, offline-first Integrated Development Environment with local AI assistance powered by Ollama. Built as a free alternative to commercial AI-powered IDEs like Cursor.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-Open-green.svg)
![AI](https://img.shields.io/badge/AI-Ollama-orange.svg)

---

## ✨ Features

- **🤖 Local AI Assistant** - Powered by Ollama (Llama 3.2, Phi 3). Works completely offline with no API keys or payments required.
- **🐍 Python Support** - Run Python code with output displayed in a dedicated panel.
- **📜 JavaScript Support** - Execute JavaScript via Node.js with full console.log support.
- **🌐 HTML Preview** - View HTML files in a built-in HTTP server with auto-launch.
- **💾 Auto-Save** - Code is automatically saved when switching between files.
- **📁 File Explorer** - Manage project files from the left sidebar.
- **⚠️ Error Detection** - Automatic error parsing with line numbers in the Problems panel.
- **💻 Integrated Terminal** - Run system commands (pip install, python, node, etc.).
- **📥 Input Panel** - Pre-enter input data for programs that require user input.
- **🖥️ Desktop Mode** - Run as a native desktop application (not just in browser).

---

## 📦 Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **OS** | Windows 10 | Windows 11 |
| **RAM** | 4 GB | 8 GB+ |
| **Storage** | 5 GB | 10 GB+ |
| **Python** | 3.8+ | 3.11+ |
| **Ollama** | Required | Latest version |
| **Node.js** | Optional (for JS) | Latest LTS |

---

## 🚀 Installation

### 1. Clone or Download the Project

```bash
git clone https://github.com/yourusername/nf-void-ide.git
cd nf-void-ide
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Ollama (Required for AI)

1. Download from: https://ollama.com/
2. Install and run the installer
3. Download a model:
   ```bash
   ollama pull phi3
   ```
   Or for better quality:
   ```bash
   ollama pull llama3.2
   ```

### 4. Install Node.js (Optional, for JavaScript)

Download from: https://nodejs.org/

---

## 🎯 Usage

### Run as Desktop Application (Recommended)

```bash
start_cursor.bat
```

Or manually:
```bash
python desktop_app.py
```

### Run in Browser

```bash
python main.py
```

Then open: `http://127.0.0.1:8000`

---

## 📁 Project Structure

```
NF_Void_IDE/
├── desktop_app.py      # Desktop application launcher
├── main.py             # Browser-based server
├── start_cursor.bat    # One-click launcher (Windows)
├── requirements.txt    # Python dependencies
├── static/
│   └── index.html      # Frontend interface
├── tmp_execution/      # Temporary files (auto-generated)
├── app.py              # Your Python code
├── *.html              # Your HTML files
└── *.js                # Your JavaScript files
```

---

## 🤖 AI Configuration

Edit `desktop_app.py` or `main.py` to change AI settings:

```python
OLLAMA_MODEL = "phi3"        # Model name
OLLAMA_HOST = "http://localhost:11434"  # Ollama server
```

### Available Models

| Model | Size | Speed | Quality |
|-------|------|-------|---------|
| `phi3` | 1.8 GB | ⚡ Fast | ⭐⭐⭐⭐ |
| `llama3.2` | 2.0 GB | ⚡ Fast | ⭐⭐⭐⭐ |
| `llama3` | 4.7 GB | 🐌 Medium | ⭐⭐⭐⭐⭐ |
| `codellama` | 3.8 GB | ⚡ Fast | ⭐⭐⭐⭐ (Code-focused) |

---

## 💡 Input Panel Usage

The Input panel allows you to pre-enter data for programs that use `input()` or `prompt()`:

1. Open the **Input** tab at the bottom
2. Enter values (one per line)
3. Press **Enter** after each value
4. Click **"✓ Use Input on Run"**
5. Click **▶ Run**

The data will be automatically passed to your program!

---

## 🛠️ Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Run Code | Click ▶ Run button |
| Save File | Click 💾 Save button |
| Ask AI | Click ✨ Ask AI button |
| Toggle Bottom Panel | Click ▼/▲ button |
| Switch Tabs | Click on tab names |

---

## 🐛 Troubleshooting

### AI Not Responding

```bash
# Check if Ollama is running
ollama list

# Restart Ollama server
ollama serve
```

### Port Already in Use

```bash
# Change port in desktop_app.py
uvicorn.run(app, host="127.0.0.1", port=8001)
```

### Module Not Found

```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

### Input Panel Not Working

1. Make sure you pressed **Enter** after typing
2. Click **"✓ Use Input on Run"** button
3. Check that values appear in the history list

---

## 📝 License

This project is open source and available under the MIT License.

---

## 🙏 Credits

- **Monaco Editor** - Code editor engine (same as VS Code)
- **Ollama** - Local AI runtime
- **FastAPI** - Backend framework
- **pywebview** - Desktop window wrapper

---
