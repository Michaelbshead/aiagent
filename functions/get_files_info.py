import os

def get_files_info(working_directory, directory=None):
    #Make a reference / base case working directory so program stays inside the correct folders.
    abs_working_directory = os.path.abspath(working_directory)
    target_dir = abs_working_directory
    if directory:
        target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(abs_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    try:
        #initilize a list
        file_list = []
        for filename in os.listdir(target_dir):
        #filename

            filepath = os.path.join(target_dir, filename) # create entire file path
            filesize = 0
            is_dir = os.path.isdir(filepath) # check if file
            filesize = os.path.getsize(filepath) #gets file size from file from entire file path
            file_list.append(f"- {filename}: file_size={filesize} bytes, is_dir={is_dir}")
        return "\n".join(file_list)
    except Exception as e:
        return f"Error listing files: {e}"
    
    #build a return string representing the contents of the firectory. It should use this format. 


    # - README.md: file_size=1032 bytes, is_dir=False
    # - src: file_size=128 bytes, is_dir=True
    # - package.json: file_size=1234 bytes, is_dir=False

