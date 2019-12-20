from sys import argv
from typing import Dict
import shutil, os

def move_all(path_source: str, path_destination: str) -> None:
    """Move all files from source to destination directory"""

    # list of source directory
    files = os.listdir(path_source)

    # checking if current directory not empty
    if files:
        
        # loop the files name
        for filename in files:

            # get file name and file extension
            name, extension = os.path.splitext(filename)
            
            # destination folder
            folder: str = f'{path_destination}/{file_folder(extension)}'
            os.makedirs(folder, exist_ok=True)

            # file source and destination
            file_source: str = f'{path_source}/{filename}'
            file_destination: str = f'{folder}/{file_rename(path_destination, filename)}'
            
            # move file
            shutil.move(file_source, file_destination)

def file_folder(extension: str) -> str:
    """Give folder for save file"""
    
    folders: Dict[str, str] = {
        # folder
        '': 'folder',

        # compressed
        '.zip': 'compressed',
        '.rar': 'compressed',

        # iso
        '.iso': 'iso',

        # text
        '.txt': 'text',

        # image
        '.jpg': 'image',
        '.png': 'image',
        '.svg': 'image',

        # video
        '.mp4': 'video',
        '.mov': 'video',
        '.3gp': 'video',

        # music
        '.mp3': 'music',
    }
    return folders[extension] if extension in folders else 'unknown'

def file_rename(path_destination: str, filename: str) -> str:
    """This is rename file if file exist in destination directory"""
    counter = 0

    # get file name and file extension
    name, extension = os.path.splitext(filename)

    # check same file name 
    while os.path.exists(f'{path_destination}/{file_folder(extension)}/{filename}'):
        counter += 1
        filename = f'{name}_{counter}{extension}'

    return filename

def main() -> None:    
    """This is the main method to call in main scope"""

    try:
        # check argv length
        if len(argv) < 3:
            # 0th param is this script name
            # 1st param is source path
            # 2nd param is destination path
            raise Exception("Make sure set source and destination path!")

        # check if path not valid
        if not os.path.exists(argv[1]) or not os.path.exists(argv[2]):
            raise Exception("Make sure source and destination path is valid!")
        
        # use argv paths
        path_source: str = os.path.normpath(argv[1])
        path_destination: str = os.path.normpath(argv[2])
        
        # operation
        move_all(path_source, path_destination)

    except Exception as e:
        print(e)


# main scope to run
if __name__ == '__main__':
    
    main()
