import os
import json
from pathlib import Path

CONFIG_DIR = Path.home() / ".scafai"
CONFIG_FILE = CONFIG_DIR / "config.json"

def get_saved_api_key() -> str | None:
    """Reads the saved OpenAI API key from ~/.scafai/config.json"""
    if CONFIG_FILE.exists():
        try:
            with CONFIG_FILE.open("r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("openai_api_key")
        except Exception:
            return None
    return None

def save_api_key(key: str):
    """Saves the OpenAI API key to ~/.scafai/config.json"""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with CONFIG_FILE.open("w", encoding="utf-8") as f:
        json.dump({"openai_api_key": key}, f)