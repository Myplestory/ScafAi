from pathlib import Path
from collections import defaultdict

EXTENSION_LANGUAGE_MAP = {
    ".py": "Python",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".java": "Java",
    ".c": "C",
    ".cpp": "C++",
    ".cs": "C#",
    ".rb": "Ruby",
    ".go": "Go",
    ".rs": "Rust",
    ".php": "PHP",
    ".swift": "Swift",
    ".kt": "Kotlin",
    ".dart": "Dart",
    ".m": "Objective-C",
    ".scala": "Scala",
    ".r": "R",
    ".sh": "Shell",
    ".html": "HTML",
    ".css": "CSS",
    ".lua": "Lua",
    ".pl": "Perl",
}

def detect_language(project_path: Path) -> str:
    """Returns the most common language in the project based on file extensions"""
    lang_count = defaultdict(int)
    for file in project_path.rglob("*.*"):
        ext = file.suffix.lower()
        if ext in EXTENSION_LANGUAGE_MAP:
            lang = EXTENSION_LANGUAGE_MAP[ext]
            lang_count[lang] += 1
    return max(lang_count.items(), key=lambda x: x[1])[0] if lang_count else "Unknown"

def get_imports(project_path: Path) -> list[str]:
    """Basic Python import scanner for now — modular per language later."""
    imports = set()
    # Temporary: Python-only import extraction
    for file in project_path.rglob("*.py"):
        try:
            with open(file, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip().startswith(("import", "from")):
                        imports.add(line.strip())
        except Exception:
            continue
    return sorted(imports)

def list_files(project_path: Path) -> list[str]:
    """Returns a list of all file paths relative to the project root."""
    return [
        str(f.relative_to(project_path))
        for f in project_path.rglob("*")
        if f.is_file()
    ]