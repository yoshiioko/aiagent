import os
from google.genai import types


def get_files_info(working_directory: str, directory: str = ".") -> str:
    """
    Lists files and directories with their sizes within the working directory.

    Args:
        working_directory: The base directory where operations are allowed
        directory: Path to list contents from, relative to working_directory (defaults to ".")

    Returns:
        str: Formatted list of files/directories with size and type information, or error message
    """
    abs_working_dir = os.path.abspath(working_directory)
    abs_directory = os.path.abspath(os.path.join(working_directory, directory))

    if not abs_directory.startswith(abs_working_dir):
        return f'Error: "{directory}" is not in the working directory'

    final_response = ""

    contents = os.listdir(abs_directory)
    for content in contents:
        content_path = os.path.join(abs_directory, content)
        is_dir = os.path.isdir(content_path)
        size = os.path.getsize(content_path)
        final_response += f"- {content}: file_size={size} bytes, is_dir={is_dir}\n"

    return final_response


# Gemini Function Calling schema for get_files_info
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
