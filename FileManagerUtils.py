import shutil

#shutil.copy(source, destination)

#shutil.move(source, destination)

#shutil.copytree(path)

import os

#print(os.getcwd())

#os.unline(path) -> deletes a single file

#os.rmdir(path) -> deletes a directory

#for filename in os.listdir('C:\\Users\\Mai\\Desktop\\'):
#    print(filename)


def FindTree(path):
    for root, dirs, files in os.walk(path):
        print(root, dirs, files, sep='\n')
    return 0


def find_files_by_type(path, filetype):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(filetype):
                print(file)
    return 0


def find_file(filename):
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file == filename:
                print(file)


def find_file_and_return_dir(filename):
    for root, dirs, files in os.walk('C:\\'):
        for file in files:
            if file == filename:
                return root + '\\' + filename
