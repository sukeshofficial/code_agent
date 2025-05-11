from agent import generate_code
import os
from rich.prompt import Prompt
from rich.console import Console
from git_utils import commit_and_push

console = Console()

def main():
    while True:
        task = Prompt.ask("\n🤖 What do you want the AI to code?")
        
        if task.lower() in ["exit", "quit"]:
            console.print("Exiting the program. Goodbye! 👋", style="bold red")
            break
        
        code, explanation = generate_code(task)
        file_name = Prompt.ask("\n💾 What do you want to name the file? (without extension)")
        file_extension = Prompt.ask("\n📂 What is the file extension? (e.g., .py, .js, .java)")
        file_path = f"{file_name}{file_extension}"
        with open(file_path, "w") as file:
            file.write(code)
        
        readme_path = "README.md"
        with open(readme_path, "a", encoding="utf-8") as readme:
            readme.write(f"\n\n## 📌 Task: {task}\n\n")
            readme.write(f"### 🧠 Explanation\n{explanation}\n")
            readme.write(f"\n### 📄 Code File: `{file_path}`\n")
        
        console.print(f"\n✅ Code generated and saved to {file_path}!", style="bold green")
        console.print("\n💻 Generated Code:\n", style="bold blue")
        console.print(code, style="bold white")
        
        commit = Prompt.ask("📝 Enter commit message")
        commit_and_push(commit, repo_path=os.getcwd())
        
if __name__ == "__main__":
    main()