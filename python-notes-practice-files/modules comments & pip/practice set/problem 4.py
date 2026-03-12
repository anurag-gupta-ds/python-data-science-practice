import os

# Specify the directory path you want to list
directory_path = "/"

try:
    # Get the list of all files and directories in the specified path
    contents = os.listdir(directory_path)

    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"Error: The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied to access '{directory_path}'.")
