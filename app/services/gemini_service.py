from google import genai

from app.core.config import GEMINI_API_KEY
from app.prompts.system_prompt import SYSTEM_PROMPT

client = genai.Client(api_key=GEMINI_API_KEY)


def chat_with_ai(message: str):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
{SYSTEM_PROMPT}

User: {message}
"""
    )

    return response.text