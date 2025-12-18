import os
from google.genai.types import FunctionDeclaration
from config import MAX_CHARS
from google.genai import types


def get_file_content(working_directory: str, file_path: str) -> str:
    """
    Reads and returns the contents of a file within the working directory.

    Args:
        working_directory: The base directory where operations are allowed
        file_path: Path to the file relative to working_directory

    Returns:
        str: File contents (truncated at MAX_CHARS), or error message
    """
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: "{file_path}" is not in the working directory'

    if not os.path.isfile(abs_file_path):
        return f'Error: "{file_path}" is not a file'

    try:
        with open(abs_file_path, "r") as file:
            file_content_string = file.read(MAX_CHARS)
            if len(file_content_string) >= MAX_CHARS:
                file_content_string += f'[...File "{file_path}" truncated at 10,000 characters]'

        return file_content_string
    except Exception as e:
        return f"Exception reading file: {e}"


# Gemini Function Calling schema for get_file_content
schema_get_file_content: FunctionDeclaration = FunctionDeclaration(
    name="get_file_content",
    description="Gets the contents of the given file as a string, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file from the working directory.",
            ),
        },
    ),
)
