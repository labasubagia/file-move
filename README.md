# File Move
This file is used to manage a directory (_source folder_) and still make it empty by moving all files to some destination directory and make it categorized.

## How to Use?
-   You have to make sure that you run **script.py**
-   You must have a **source folder** as a folder to still keep clean
-   You must have a **destination folder** as folder destination to move the file	

#### Example :
- source folder path : _/home/user/downloads_
- destination folder path : _/home/user/manage-downloads_
```sh
$ python3 script.py /home/user/downloads /home/user/manage-downloads
```
## How to add more file types?
Steps if you want to add more file extension or file folder
1. Open **script.py** 
2. Find **file_folder** method 
3. Edit the **folders** dictionary variable 
4. Add extenstion file or folder name 
>You can customize that extension or folder based on your needs
