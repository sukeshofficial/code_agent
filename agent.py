import requests
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPEN_ROUTER_API_KEY")

def generate_code(task):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant that generates ONLY code and its explanation. Respond in two parts: first with only code between triple backticks, then a plain explanation."
            },
            {
                "role": "user",
                "content": f"Write a code for: {task}."
            }
        ],
        "temperature": 0.3,
        "max_tokens": 5000
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        if "choices" in result:
            content = result["choices"][0]["message"]["content"].strip()

            import re
            code_match = re.search(r"```(?:\w+\n)?(.*?)```", content, re.DOTALL)
            code = code_match.group(1).strip() if code_match else ""
            explanation = content.replace(code_match.group(0), "").strip() if code_match else ""

            return code, explanation

        else:
            return "", f"❌ Unexpected response: {result}"

    except Exception as e:
        return "", f"⚠️ Exception: {str(e)}"
