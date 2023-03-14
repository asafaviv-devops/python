
import os
import shutil
from sys import path

def create_file_and_write_to_it(path1, what_to_write ):
    file1= open(path1,"wb")
    file1.write(what_to_write)
    file1.close()
    pass

def delete_a_file(path1):
    os.remove(path1)
    pass

def check_if_file_exist(path_to_a_file):
    if os.path.exists(path_to_a_file):
        print("this file exist {}".format(path_to_a_file))
        return True
    else:
        print("file doesn't exist {}".format(path_to_a_file))
        return False

if __name__ == '__main__':
    path_to_a_file="C:\\tmp\\111.txt"
    create_file_and_write_to_it(path_to_a_file,"hiiiiii".encode('utf-8'))
    res1= check_if_file_exist(path_to_a_file)
    delete_a_file(path_to_a_file)
    res2= check_if_file_exist(path_to_a_file)
    list1=["a","v","a"]
    list1.remove("a")
    print(list1)

    x=10
    while x>2:
        print(x)
        x=x-1



