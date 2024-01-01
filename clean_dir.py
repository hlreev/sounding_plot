import os
import shutil

def delete_files_in_directory(directory):
    try:
        # Iterate over all files in the directory
        for file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)

            # Check if it is a file
            if os.path.isfile(file_path):
                # Delete the file
                os.remove(file_path)
                print(f"Deleted: {file_path}")

        print(f"\nAll files in '{directory}' deleted successfully.\n")
    except Exception as e:
        print(f"Error deleting files in '{directory}': {e}")

if __name__ == "__main__":
    # List of directories to delete files from
    directories_to_clear = [
        'soundings',
        'data\\level1\\',
        'viewer'
    ]

    # Delete files in each specified directory
    for directory in directories_to_clear:
        delete_files_in_directory(directory)