# -*- coding: UTF-8 -*-

import sys
from PIL import Image
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

m_ext = ".TGA"
cwd = os.getcwd()
files = get_all_file_with_extention(cwd,m_ext)



argv = sys.argv

if not len(argv) == 4:
    print("pass arguments r g b!!!")
    exit(1)
else:
    print(argv)

r = int(argv[1])
g = int(argv[2])
b = int(argv[3])

if r > 2 or g >2 or b > 2:
    print("r g b must < 2")
    exit(1)

if r == 0 and g==1 and b== 2:
     print("r=0 g=1 b=2 !! nothing need to do")
     exit(1)

for file in files:
    with Image.open(file) as im:

        print("Processing image file {name}".format(name=file))
        orig_pixel_map = im.load()
        for x in range(im.width):
            for y in range(im.height):
                xy = x,y
                color = orig_pixel_map[x,y]
                new_r = color[r]
                new_g = color[g]
                new_b = color[b]
                new_pixel = (new_r,new_g,new_b)
                orig_pixel_map[x,y] = new_pixel
        im.save(file)

        
