import os
import subprocess
from google.genai import types
from google.genai.types import FunctionDeclaration


def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    """
    Runs a Python file with the python3 interpreter.

    Args:
        working_directory: The base directory where operations are allowed
        file_path: Path to the Python file relative to working_directory
        args: Optional list of CLI arguments to pass to the Python file

    Returns:
        str: Combined stdout/stderr output and exit code information
    """
    if args is None:
        args = []

    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: "{file_path}" is not in the working directory'

    if not os.path.isfile(abs_file_path):
        return f'Error: "{file_path}" is not a file'

    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a python file'

    try:
        final_args = ['python3', file_path] + args
        output = subprocess.run(
            final_args,
            cwd=abs_working_directory,
            timeout=30,
            capture_output=True
        )

        final_output = f"""
STDOUT: {output.stdout.decode('utf-8')}
STDERR: {output.stderr.decode('utf-8')}
"""

        if output.stdout == "" and output.stderr == "":
            final_output = "No output produced.\n"

        if output.returncode != 0:
            final_output += f"Process exited with code {output.returncode}\n"

        return final_output

    except Exception as e:
        return f'Error: executing Python file: {e}'


# Gemini Function Calling schema for run_python_file
schema_run_python_file: FunctionDeclaration = FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file with the python3 interpreter. Accepts additional CLI args as an optional array.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to run, relative to the working directory."
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="An optional array of strings to be used as the CLI args for the Python file.",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
    ),
)
