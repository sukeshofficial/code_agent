
# 🤖 CodeAgent

**An Autonomous Agent for Completing, Debugging, and Uploading Code to GitHub**

---

## 📌 Description

CodeAgent is an intelligent autonomous coding agent that takes a **coding API/task as input**, completes the task, generates the final code in a new file, and **automatically pushes the result to GitHub**. It can also **debug** and **refactor** code as needed using agentic workflows.

This is **SukeshOfficial's first Code Agent project**, designed to demonstrate intelligent end-to-end software automation.

---

## 👨‍💻 Author

**SukeshOfficial**  
GitHub: [@sukeshofficial](https://github.com/sukeshofficial)

---

## 📁 Project Structure

```
.
├── .vscode/             # VS Code workspace settings
├── .gitignore           # Git ignored files list
├── BinarySearch.java    # Example task output file
├── README.md            # Project documentation
├── agent.py             # Core agent logic
├── cli.py               # Command-line interface for interacting with the agent
├── git_utils.py         # GitHub integration and automation utilities
```

---

## ⚙️ Features

- ✅ Takes coding task or API as input
- 🧠 Uses an agentic model to solve or debug the problem
- 📄 Generates new output files (e.g., `.py`, `.java`, etc.)
- 🚀 Automatically commits and pushes changes to GitHub
- 🐞 Useful for debugging and automated PR workflows

---

## 🚀 How It Works

1. **Input**: User provides a prompt or API instruction (e.g., “Create a binary search in Java”)
2. **Agent Engine**: `agent.py` interprets the task using a coding LLM
3. **File Generation**: Creates the output code in a new file (e.g., `BinarySearch.java`)
4. **Git Automation**: `git_utils.py` commits and pushes to the GitHub repository

---

## 🛠️ Setup Instructions

```bash
git clone https://github.com/sukeshofficial/code_agent.git
cd code_agent

# Optional: Create virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 🔄 Run the Agent

```bash
python cli.py --task "Create a Python script to calculate factorial using recursion"
```

> Output will be saved in a new `.py` file and automatically pushed to GitHub.

---

## 🔐 Environment Variables

You may use a `.env` file to store your GitHub token:

```env
GITHUB_TOKEN=your_personal_access_token
```

Ensure `.env` is listed in `.gitignore`.

---

## 📜 License

MIT License

---

**🚀 Built by SukeshOfficial**
