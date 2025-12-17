import os


def write_file(working_directory, file_path, content):
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
