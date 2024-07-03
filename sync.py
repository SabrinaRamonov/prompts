import os
import shutil

#
# Sync all my fabric patterns to my public prompt library
#

# Define the source and destination directories
source_dir = os.path.expanduser("~/.config/fabric/patterns/")
dest_dir = os.path.expanduser("~/Dev/prompts/")

# Ensure the destination directory exists
try:
    os.makedirs(dest_dir, exist_ok=True)
    print(f"Destination directory '{dest_dir}' is ready.")
except Exception as e:
    print(f"Error creating destination directory '{dest_dir}': {e}")
    exit(1)

# Iterate through each directory in the source directory
try:
    for subdir in os.listdir(source_dir):
        subdir_path = os.path.join(source_dir, subdir)

        # Check if the current item is a directory
        if os.path.isdir(subdir_path):
            source_file = os.path.join(subdir_path, "system.md")

            # Check if the system.md file exists in the current directory
            if os.path.isfile(source_file):
                dest_file = os.path.join(dest_dir, f"{subdir}.md")

                # Copy the file to the destination directory with the new name
                try:
                    shutil.copy(source_file, dest_file)
                    print(f"Copied '{source_file}' to '{dest_file}'")
                except Exception as e:
                    print(f"Error copying '{source_file}' to '{dest_file}': {e}")
            else:
                print(f"No 'system.md' file found in '{subdir_path}'")
        else:
            print(f"'{subdir_path}' is not a directory")
except Exception as e:
    print(f"Error processing directories in '{source_dir}': {e}")
    exit(1)

print("All eligible files have been copied.")
