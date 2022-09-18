
import os

def get_all_file_with_extention(directory,extention):
    '''
        example : all_csv = get_all_file_with_extention(data_dir,".csv")
    '''
    folder_list = os.listdir(directory)
    fbx_name_list = []
    for i in folder_list:
        if os.path.splitext(i)[1] == extention:
            fbx_name_list.append(i)
    return fbx_name_list


# Get Script Directory
# print(os.path.dirname(os.path.realpath(__file__)))