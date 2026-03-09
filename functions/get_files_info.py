import os
from google.genai import types

def get_files_info(working_directory, directory='.'):
    
    try:
        current_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(current_dir, directory))
        valid_target_dir = os.path.commonpath([current_dir, target_dir]) == current_dir
        string_to_return = ''

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        for item in os.listdir(target_dir):
            item_path = os.path.join(target_dir, item)
            item_size = os.path.getsize(item_path)
            item_type = os.path.isdir(item_path)
            string_to_return += f'- {item}: file_size={item_size} bytes, is_dir={item_type}\n'

        return string_to_return
    except Exception as e:
        return f'Error: {str(e)}'
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)