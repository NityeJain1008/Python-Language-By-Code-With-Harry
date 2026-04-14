# Program to print contents of a directory using os module

import os

# you can give a specific path OR leave empty for current folder

path = "."      # "." means current directory

# get list of files and folders

contents = os.listdir(path)

print("Contents of the directory are:\n")

# print each item one by one

for item in contents:
    print(item)
