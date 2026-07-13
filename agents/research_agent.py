import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


MODEL = "openai/gpt-oss-20b:free"

def research_app(app_name):

    prompt = f"""
You are an AI Product Operations Researcher.

Research the SaaS application:

{app_name}

Use official documentation whenever possible.

If information cannot be verified,
return "Unknown".

Return ONLY valid JSON.

Schema:

{{
    "app":"",
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
- Return only JSON.
- No markdown.
- No explanation.
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    text = response.choices[0].message.content.strip()

    if text.startswith("```"):
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

    return json.loads(text)


if __name__ == "__main__":

    app = input("Enter App Name: ")

    result = research_app(app)

    print(json.dumps(result, indent=4))

    os.makedirs("output", exist_ok=True)

    filename = app.lower().replace(" ", "_").replace("/", "_") + ".json"

    with open(
        f"output/{filename}",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(result, f, indent=4)

    print(f"\nSaved to output/{filename}")