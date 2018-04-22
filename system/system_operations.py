import os


def touch(path):
    with open(path, 'a'):
        os.utime(path, None)


def get_line_number(search, path):
    with open(path) as myFile:
        for num, line in enumerate(myFile, 0):
            if search in line:
                return num


def write_file(path, file_edited):
    with open(path, 'w') as myFile:
        myFile.writelines(file_edited)


def remove_path_if_exists(path_file):
    if os.path.exists(path_file):
        os.remove(path_file)