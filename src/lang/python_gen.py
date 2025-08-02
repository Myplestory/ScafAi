from generator import call_gpt

def generate_readme(project_name, files, imports, model="gpt-4o", temperature=0.7):
    prompt = f"""
Generate a professional README.md for a Python project called "{project_name}".
Files: {files}
Imports: {imports}
Include sections: Title, Description, Installation, Usage, License.
"""
    return call_gpt(prompt, model=model, temperature=temperature)

def generate_gitignore(model="gpt-4o", temperature=0.7):
    prompt = "Generate a .gitignore file for a Python project."
    return call_gpt(prompt, model=model, temperature=temperature)

def generate_dependencies(imports, model="gpt-4o", temperature=0.7):
    prompt = f"""
Generate a requirements.txt file from these Python imports (only third-party packages):
{imports}
"""
    return call_gpt(prompt, model=model, temperature=temperature)
