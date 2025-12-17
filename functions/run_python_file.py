import os
import subprocess


def run_python_file(working_directory: str, file_path: str, args=None) -> str:
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
