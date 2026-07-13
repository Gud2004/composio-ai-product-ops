import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL = "gemini-3.5-flash"


def research_app(app_name: str):
    prompt = f"""
You are an AI Product Operations researcher.

Research the SaaS application: {app_name}

Return ONLY valid JSON.

Schema:

{{
"name":"",
"category":"",
"description":"",
"authentication":"",
"self_serve":"",
"api_surface":"",
"mcp":"",
"buildability":"",
"main_blocker":"",
"evidence":[]
}}

Rules:

- Do not explain.
- No markdown.
- No code blocks.
- Evidence should contain official documentation URLs whenever possible.
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return json.loads(response.text)


if __name__ == "__main__":
    result = research_app("Slack")

    print(json.dumps(result, indent=4))