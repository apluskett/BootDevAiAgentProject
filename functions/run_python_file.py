import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        current_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(current_dir, file_path))
        valid_target_file = os.path.commonpath([current_dir, target_file]) == current_dir

        if not valid_target_file:
                return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
            
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not target_file.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        command = ['python3', target_file]
        
        if args:
            command.extend(args)

        command_results_capture = subprocess.run(command, capture_output=True, text=True, timeout=30, cwd=current_dir)
        if command_results_capture.returncode != 0:
            return f'Process exited with code {command_results_capture.returncode}'
        if not command_results_capture.stderr and not command_results_capture.stdout:
            return 'No output produced'
        else:
            return f'STDOUT:\n{command_results_capture.stdout}\nSTDERR:\n{command_results_capture.stderr}'
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file and returns its output",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional list of string arguments to pass to the Python file when executing",
            )
        },
        required=["file_path"]
    ),
)
        