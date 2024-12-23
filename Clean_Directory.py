import os
import shutil

def clear_folder(path):
    # Check if the folder exists
    if not os.path.exists(path):
        print(f"The folder '{path}' does not exist.")
        return

    # Iterate through the contents of the folder
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        try:
            # Check if it is a file or a folder
            if os.path.isfile(item_path) or os.path.islink(item_path):  # File or symbolic link
                os.unlink(item_path)  # Delete the file
                print(f"Deleted file: {item_path}")
            elif os.path.isdir(item_path):  # Directory
                shutil.rmtree(item_path)  # Delete the folder
                print(f"Deleted folder: {item_path}")
        except Exception as e:
            print(f"Failed to delete {item_path}: {e}")


