import os
from google.genai import types
from google.genai.types import FunctionDeclaration


def write_file(working_directory: str, file_path: str, content: str) -> str:
    """
    Writes content of a file, creating parent directories if needed.

    Args:
        working_directory: The base directory where operations are allowed
        file_path: Path to the file relative to working_directory
        content: String content to write to the file

    Returns:
        str: Success message with character count or error message.
    """
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: "{file_path}" is not in the working directory'

    parent_directory = os.path.dirname(abs_file_path)
    if not os.path.isdir(parent_directory):
        try:
            os.makedirs(parent_directory)
        except Exception as e:
            return f'Could not create parent directories: {parent_directory} = {e}'

    try:
        with open(abs_file_path, "w") as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" {len(content)} characters written'
    except Exception as e:
        return f"Failed to write to file: {file_path}, {e}"


# Gemini Function Calling schema for write_file
schema_write_file: FunctionDeclaration = FunctionDeclaration(
    name="write_file",
    description="Overwrites an existing file or writes to a new file if it doesn't exist (and creates required parent directories safely), constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write."
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The contents to write to the file as a string."
            ),
        },
    ),
)
