import os
import shutil
from typing import List


def check_if_path_exists(input_dir):
    path_exists = os.path.exists(input_dir)
    is_dir = os.path.isdir(input_dir)
    is_file = os.path.isfile(input_dir)
    return path_exists, is_dir, is_file


def create_directory(file_dir):
    try:
        # os.makedirs() method in Python is used to create a directory recursively.
        # That means while making leaf directory if any intermediate-level directory is missing, os.makedirs() method will create them all.
        os.mkdir(file_dir)
    except OSError as error:
        print(f"Error Creating the directory {file_dir}. Below is teh error message:")
        print(error)


def create_files(file_dir: str, filename: str):
    file_path = join_path(file_dir, filename)
    file = open(file_path, "w+")
    for i in range(10):
        file.write(f"This is line {i} in the file {filename}\n")
    file.close()


def join_path(dirname: str, filename: str) -> str:
    return os.path.join(dirname, filename)


def move_file(srcpath, destpath):
    print(f"Moving file from :{srcpath} to:{destpath}")
    _, _, is_file = check_if_path_exists(srcpath)
    if is_file:
        haspath, isdir, is_file = check_if_path_exists(destpath)
        if is_file:
            destdir, _ = os.path.split(destpath)
            delete_dir(destdir)
        elif not haspath:
            create_directory(destpath)
        shutil.move(srcpath, destpath)
    else:
        print(f"Source path must be a valid file. But the given source path : {srcpath} is not a valid file.")


def rename_file(filepath, oldname, newname):
    path_exists, is_dir, is_file = check_if_path_exists(filepath)
    oldpath, newpath = join_path(filepath, oldname), join_path(filepath, newname)
    if is_file:
        os.rename(oldpath, newpath)


def copy_file(srcpath, destpath):
    path_exists, is_dir, is_file = check_if_path_exists(srcpath)
    if path_exists and is_file:
        path_exists, is_dir, is_file = check_if_path_exists(destpath)
        if is_file:
            print('Destination is a file, it should be a directory.')
            print("Kindly enter a valid destination directory.")
        else:
            if not path_exists:
                print("The destination is not a valid directory. Creating a new directory.")
                create_directory(destpath)
            shutil.copy(srcpath, destpath)
    else:
        print(f"The source path must be a valid file.")


def open_and_read_file(name):
    file = open(name)
    file_input = file.readlines()
    file.close()
    return file_input


def open_and_read_all_in_file(name):
    file = open(name)
    file_input = file.read()
    file.close()
    return file_input


def get_current_working_directory():
    cwd = os.getcwd()
    return cwd


def list_all_files(input_dir=get_current_working_directory()) -> List:
    dir_files = os.listdir(input_dir)
    return dir_files


def list_all_files_recursively(input_dir: str) -> List:
    return [(cur_dir, sub_dir, files) for cur_dir, sub_dir, files in os.walk(input_dir)]


def zip_file(dirname, ziptype, zipname):
    _, isdir, _ = check_if_path_exists(dirname)
    if isdir:
        shutil.make_archive(zipname, ziptype, dirname)


def delete_file(filepath):
    print(f"Deleting the file : {filepath}")
    _, isdir, isfile = check_if_path_exists(filepath)
    if isfile:
        os.remove(filepath)
    elif isdir:
        print("Given path is not a file, its a directory. Deleting the whole directory.")
        delete_dir(filepath)
    else:
        print(f"Could not delete, as it not a file.")


def delete_dir(filepath):
    print(f"Deleting the directory : {filepath}")
    path_exists, isdir, _ = check_if_path_exists(filepath)
    if path_exists and isdir:
        shutil.rmtree(filepath)


file_name = "print_and_scan_input.py"
different_dir = "D:\\Projects\\Python\\first-python-project\\io_file"
new_dir = "D:\\Projects\\Python\\first-python-project\\io_file\\files"
new_file_names = ["file_" + str(i) + ".txt" for i in range(10)]

print("*******************************")
print(f"Creating directory: {new_dir}")
create_directory(new_dir)

print("*******************************")
print(f"Creating files: {new_file_names}")
for filename in new_file_names:
    create_files(new_dir, filename)

print("*******************************")
files_recursively = list_all_files_recursively(new_dir)
print(f"List all files recursively in {new_dir} directory before moving : \n{files_recursively}")

print("*******************************")
print(open_and_read_file(file_name))

print("*******************************")
print(open_and_read_all_in_file(file_name))
print(open_and_read_all_in_file(join_path(new_dir, new_file_names[1])))

print("*******************************")
print("Moving odd number files to odd folder, and even to even folder.")
odd_dir = join_path(new_dir, "odd")
even_dir = join_path(new_dir, "even")
for filename in new_file_names:
    split = filename.split(".")
    lastchar = split[0][len(split[0]) - 1]
    lastnum = int(lastchar)
    file_path = join_path(new_dir, filename)
    if lastnum % 2 == 0:
        move_file(file_path, even_dir)
    else:
        move_file(file_path, odd_dir)

print("*******************************")
print(f"Get the current Directory : {get_current_working_directory()}")

print("*******************************")
print(f"List all files in current directory : {list_all_files()}")

print("*******************************")
files_recursively = list_all_files_recursively(new_dir)
print(f"List all files recursively in {new_dir} directory : {files_recursively}")

print("*******************************")
print(f"List all files in {even_dir} directory : {list_all_files(even_dir)}")
print(f"List all files in {odd_dir} directory : {list_all_files(odd_dir)}")

print("*******************************")
print("Deleting all the test files created.")
for path, _, files in files_recursively:
    for file in files:
        delete_file(join_path(path, file))

print("*******************************")
print("Deleting all the test directories.")
delete_dir(new_dir)
