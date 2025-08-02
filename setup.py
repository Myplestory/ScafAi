from setuptools import setup, find_packages

setup(
    name="scafai",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "typer>=0.9.0",
        "openai",
    ],
    entry_points={
        "console_scripts": [
            "scafai=main:app",  # because src/main.py has `app = typer.Typer()`
        ],
    },
    python_requires=">=3.8",
)
