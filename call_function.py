from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file
from google.genai import types


working_directory = "calculator"


def call_function(function_call_part: types.Part, verbose: bool = False) -> types.Content:
    """
    Routes and executes function calls from the AI agent, returning results as tool responses.

    Args:
        function_call_part: The function call part containing name and arguments
        verbose: Whether to print detailed function call information (defaults to False)

    Returns:
        types.Content: Tool response containing function result or error message
    """
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f"Calling function: {function_call_part.name}")

    result = ""
    if function_call_part.name == "get_files_info":
        result = get_files_info(working_directory, **function_call_part.args)
    if function_call_part.name == "get_file_content":
        result = get_file_content(working_directory, **function_call_part.args)
    if function_call_part.name == "write_file":
        result = write_file(working_directory, **function_call_part.args)
    if function_call_part.name == "run_python_file":
        result = run_python_file(working_directory, **function_call_part.args)

    if result == "":
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": result},
            )
        ],
    )
