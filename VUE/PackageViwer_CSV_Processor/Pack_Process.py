import csv
import pandas as pd
import os
from datetime import date
today = date.today()

def get_all_file_with_extention(directory,extention):
    folder_list = os.listdir(directory)
    fbx_name_list = []
    for i in folder_list:
        if os.path.splitext(i)[1] == extention:
            fbx_name_list.append(i)
    return fbx_name_list

data_relative = "/14_1/08_17/"
script_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = script_dir + data_relative

all_csv = get_all_file_with_extention(data_dir,".csv")
for csv_file_name in all_csv:
    csv_file_path = data_dir + csv_file_name
    f = open(csv_file_path,'r')
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        Path = row[" Path"].lstrip()
        Class = row[" Class"].lstrip()
        c_Size = row[" Compressed Size"].lstrip()
        if Class == " uptnl":
            print(c_Size)
