"""
File handling modes:
1) r : read if exist
2) w : write if exist, create if not, override possible
3) a : append file if exists, no create, no override
4) x : create file for writing, fail if already present
# b is used for binary and + signify that mode can be modified i.e. read + write
5) r+: read and write, data can be overwritten
6) w+: write and read, data can be overwritten
7) a+: append and read, data can not be overwritten

# All the above function are also available to read in binary form, can be used by appending b in mode, i.e. rb, wb, ab.(not +)

methods:
read(): Reads the entire file content.
readline(): Reads one line at a time.
readlines(): Reads all lines into a list.
write(): Writes a string to the file.
writelines(): Writes a list of lines to the file.
open and close.

# learn about context managers and with statement.
with: It handles the file closing when user is done, even if any error occurs and prevent any data loss.
"""  
import os

def file_exists(filepath:str):
    return os.path.exists(filepath)

def read_file(filepath:str):
    if not file_exists(filepath):
        print(f"{filepath} not found")
        return
    
    with open(filepath) as file:
        data = file.read()
        if data =="":
            print("Empty file.")
            return
        print(data)

def create_file(filepath:str):
    if file_exists(filepath):
       print(f"{filepath} already exists.")
       return
    open(filepath, 'x')

def write_file(filepath:str, *data):
    with open(filepath, 'w') as file:
        file.writelines(data)

def append_file(filepath:str, *data):
    if not file_exists(filepath):
        print(f"{filepath} not exists.")
        return 
    
    with open(filepath, 'a') as file:
        # file.writelines(data) # writes in single line 
        for line in data:
            file.write(line+"\n")
 
def rename_file(filename:str, new_filename:str):
    if not file_exists(filename):
        print(f"{filename} not exists.")
        return 

    os.rename(filename, new_filename)
    print("File " + filename + " renamed to " + new_filename + " successfully.")

 
def delete_file(filename):
    if not file_exists(filename):
        print(f"{filename} not exists.")
        return 
    
    os.remove(filename)
    print("File " + filename + " deleted successfully.")


if __name__== '__main__':
    read_file('example.txt')
    create_file('example.txt')
    read_file('example.txt')
    write_file('example.txt', "this is shrey jain\n")
    read_file('example.txt')
    append_file('example.txt', "Line 2", "Line 3")
    read_file('example.txt')
    rename_file('example.txt', "my_file.txt")
    read_file('my_file.txt')
    delete_file('my_file.txt')
    read_file('my_file.txt')
