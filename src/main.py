import os
import typer
from pathlib import Path

from scan import detect_language, get_imports, list_files
from lang import get_generator
from config import get_saved_api_key, save_api_key
from generator import set_api_key

app = typer.Typer()

@app.command()
def generate(
    path: Path,
    model: str = typer.Option("gpt-4o", help="OpenAI model to use (e.g. gpt-4o, gpt-3.5-turbo)"),
    temperature: float = typer.Option(0.7, help="Creativity level (0.0 = deterministic, 1.0 = creative)")
):
    if not path.exists():
        typer.echo("❌ Provided path does not exist.")
        raise typer.Exit(1)

    api_key = os.getenv("OPENAI_API_KEY") or get_saved_api_key()
    if not api_key:
        api_key = typer.prompt("🔐 Enter your OpenAI API key")
        save_api_key(api_key)
    set_api_key(api_key)

    project_name = path.name
    language = detect_language(path)
    files = list_files(path)
    imports = get_imports(path)

    typer.echo(f"🔍 Detected language: {language}")

    gen = get_generator(language)

    typer.echo("📄 Generating README.md...")
    readme = gen.generate_readme(project_name, files, imports, model=model, temperature=temperature)
    (path / "README.md").write_text(readme)

    typer.echo("📄 Generating .gitignore...")
    gitignore = gen.generate_gitignore(model=model, temperature=temperature)
    (path / ".gitignore").write_text(gitignore)

    typer.echo("📄 Generating dependencies file...")
    deps = gen.generate_dependencies(imports, model=model, temperature=temperature)
    (path / "requirements.txt").write_text(deps)

    typer.echo("✅ Done!")

if __name__ == "__main__":
    app()