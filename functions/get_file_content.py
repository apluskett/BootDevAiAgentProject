import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    try:
        current_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(current_dir, file_path))
        valid_target_file = os.path.commonpath([current_dir, target_file]) == current_dir

        if not valid_target_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        #I would change this to make it a little more readable that the file is being truncated by
        #changing the content variable in the if to read as: content = '{exceed} \n {f.read(MAX_CHARS)} \n {exceed}'
        with open(target_file, 'r') as f:
            content = f.read(MAX_CHARS)
            if f.read(1):
                content += f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        
        return content
    
    except Exception as e:
        return f'Error: {str(e)}'

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads content from a specified file relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to read from, relative to the working directory",
            )
        },
        required=["file_path"]
    ),
)