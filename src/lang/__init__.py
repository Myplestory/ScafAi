from importlib import import_module
from . import default_gen

def get_generator(language: str):
    lang = language.lower()
    try:
        return import_module(f"src.lang.{lang}_gen")
    except ModuleNotFoundError:
        return default_gen
