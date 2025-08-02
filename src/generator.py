import os
from openai import OpenAI


def set_api_key(key: str):
    """Sets the OpenAI API key."""
    os.environ["OPENAI_API_KEY"] = key

def call_gpt(prompt: str, model: str = "gpt-4o", temperature: float = 0.7) -> str:
    client = OpenAI()
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )
    return response.choices[0].message.content.strip()