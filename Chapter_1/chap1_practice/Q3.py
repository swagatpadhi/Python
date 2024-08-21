import os

# Get the current working directory
current_directory = os.getcwd()

# Specify the directory you want to list (use '.' for the current directory)
directory_path = 'C:/Users/swaga/Desktop/movies'

# Print the current working directory
print("Current Directory:", current_directory)

# Get the list of files and directories in the specified path
contents = os.listdir(directory_path)

# Print each item in the directory
for item in contents:
    print(item)
