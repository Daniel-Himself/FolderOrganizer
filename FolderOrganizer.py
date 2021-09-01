# FolderOrganizer.py
# How to use instructions are located in the README.md file in the script's repository
import os
from shutil import move

# Directory paths
user = os.getenv('USER')
# Replace directory paths below with your desired directory path
root_dir = '/Users/Daniel/Downloads/'.format(user)
image_dir = '/Users/Daniel/Downloads/Downloaded Images/'.format(user)
documents_dir = '/Users/Daniel/Downloads/Downloaded Documents/'.format(user)
software_dir = '/Users/Daniel/Downloads/Downloaded Software/'.format(user)
# Categorized file types
doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff')
software_types = ('.exe', '.pkg', '.dmg', 'msi')


# Gets all the non-hidden files from the Download folder excluding the current script
def get_non_hidden_files_except_current_file(root_dir):
    return [f for f in os.listdir(root_dir)
            if os.path.isfile(f) and not f.startswith('.') and not f.__eq__(__file__)]


# Takes the list of files and moves them to there respective folders
def move_files(files):
    for file in files:
        # file moved and overwritten if already exists
        if file.endswith(doc_types):
            move(file, '{}/{}'.format(documents_dir, file))
            print('file {} moved to {}'.format(file, documents_dir))
        elif file.endswith(img_types):
            move(file, '{}/{}'.format(image_dir, file))
            print('file {} moved to {}'.format(file, image_dir))
        elif file.endswith(software_types):
            move(file, '{}/{}'.format(software_dir, file))
            print('file {} moved to {}'.format(file, software_dir))


if __name__ == "__main__":
    files = get_non_hidden_files_except_current_file(root_dir)
move_files(files)
