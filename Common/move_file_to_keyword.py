from copy import copy
from genericpath import isdir
import os
from pathlib import Path
import shutil
from symbol import tfpdef


def get_all_file_with_keyword(directory,keyworld):
    '''
        example : all_csv = get_all_file_with_extention(data_dir,".csv")
    '''
    folder_list = os.listdir(directory)
    fbx_name_list = []
    for i in folder_list:
        if os.path.isdir(directory+"/"+i):
            continue
        if keyworld in i:
            fbx_name_list.append(i)
    return fbx_name_list


mKeyword = "optional"
cwd = os.getcwd()
files = get_all_file_with_keyword(cwd,mKeyword)

target_directory = cwd + "/" + mKeyword
target_dir_obj = Path(target_directory)

if not target_dir_obj.exists():
    '''Create A Directory'''
    os.mkdir(target_directory)
    print("Create a directory to : {td}".format(td=target_directory))



index = 0
for f in files:
    print(index)
    filepath = cwd+"/"+f
    tarrget_file_path = target_directory+"/"+f
    print("target file path : {tfp}".format(tfp=tarrget_file_path))
    print(filepath)
    print(tarrget_file_path)
    shutil.move(filepath,tarrget_file_path) # if filepath is a directory,but target file path is a file. It will cause PermissionError:[Errno 13]
    index +=1

