from sys import argv
from typing import Dict
import shutil, os, time, datetime

# run `pip install watchdog` for these package below to work 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def move_all(path_source: str, path_destination: str) -> None:
    """Move all files from source to destination directory"""

    # list of source directory
    files = os.listdir(path_source)

    # checking if current directory not empty
    if files:
        
        # loop the files name
        for filename in files:

            # get file name and file extension
            # use _ for name because its never used
            _, extension = os.path.splitext(filename)
            
            # destination folder
            folder: str = f'{path_destination}/{file_folder(extension)}'
            os.makedirs(folder, exist_ok=True)

            # file source and destination
            file_source: str = f'{path_source}/{filename}'
            file_destination: str = f'{folder}/{file_rename(path_destination, filename)}'
            
            # move file
            shutil.move(file_source, file_destination)

            # log
            log_move(file_source, file_destination)


def file_folder(extension: str) -> str:
    """Give folder for save file"""
    
    # NOTE: You can add or customize file type or folder name on `folders` dictionary variable below
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

def log_move(file_source: str, file_destination: str, file: str = 'history.txt') -> None:
    """Log moving file and save into a file"""

    # create a message with time, source and destination moved 
    current_time: str = datetime.datetime.now()
    message: str = f'{current_time}  Move {file_source} to {file_destination}'
    
    # log message in terminal
    print(message)

    # make move history and put it into a text file
    # open file with append mode 
    history_file  = open(file, 'a+')

    # append file with message
    history_file.write(f'{message}\n')


class FileHandler(FileSystemEventHandler):
    """This class use for watch the directory"""

    path_source: str
    path_destination: str

    # constructor used to pass path source and path destination
    def __init__(self, src: str, to: str):
        self.path_source = src
        self.path_destination = to        

    # on_modified event actually is an event from filesystem event handler
    # on_modified event occurs when user create, edit, move or delete file or folder 
    def on_modified(self, event) -> None:
        """Move file on modified event"""

        # move file and keep the source folder clean
        move_all(self.path_source, self.path_destination)


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
        
        # event handler for move file
        event_handler = FileHandler(src=path_source, to=path_destination)

        # track the source file
        observer = Observer()
        observer.schedule(event_handler, path_source, recursive=True)
        observer.start()

        # run the observer to track path source until user stop it 
        try:
            # run program 
            while True:

                # sleep until 10 minutes
                time.sleep(10)

        except KeyboardInterrupt:
            # user stop the observer using Ctrl+C
            observer.stop()

        observer.join()

    except Exception as e:
        print(e)


# main scope to run
if __name__ == '__main__':
    main()
