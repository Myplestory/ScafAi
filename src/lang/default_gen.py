from generator import call_gpt

def generate_readme(project_name, files, imports, model="gpt-4o", temperature=0.7):
    prompt = f"""
Generate a README.md for a generic software project called "{project_name}".
Here are the files: {files}
Here are the detected dependencies: {imports}
Include sections: Title, Description, Installation, Usage.
"""
    return call_gpt(prompt, model=model, temperature=temperature)

def generate_gitignore(model="gpt-4o", temperature=0.7):
    prompt = "Generate a general-purpose .gitignore file."
    return call_gpt(prompt, model=model, temperature=temperature)

def generate_dependencies(imports, model="gpt-4o", temperature=0.7):
    return "No known dependency format for this language.\n"
