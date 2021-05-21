import bpy 
import math 
from mathutils import Matrix
import bmesh
import os

#Remove Blender Default Cube Mesh......
if "Cube" in bpy.data.meshes:
    mesh = bpy.data.meshes["Cube"]
    print("removing mesh", mesh)
    bpy.data.meshes.remove(mesh)


#=============================================================================

file = open('CODM_Build_02.csv','r')

lines = file.readlines()


verticesDic={}
#uvDic={}
uvss=[]
faces = []
uv_co = []

length = len(lines)
i = 1

while i < length:
    line0 = lines[i]
    line1 = lines[i+1]
    line2 = lines[i+2]

    tokens0 = line0.split(',')
    tokens1 = line1.split(',')
    tokens2 = line2.split(',')

    faces.append([int(tokens0[1]),int(tokens1[1]),int(tokens2[1])])

    uvss.append([float(tokens0[9]),float(tokens0[10])])
    uvss.append([float(tokens1[9]),float(tokens1[10])])
    uvss.append([float(tokens2[9]),float(tokens2[10])])

    verticesDic[tokens0[1]]=[float(tokens0[2]),float(tokens0[3]),float(tokens0[4])]
    verticesDic[tokens1[1]]=[float(tokens1[2]),float(tokens1[3]),float(tokens1[4])]
    verticesDic[tokens2[1]]=[float(tokens2[2]),float(tokens2[3]),float(tokens2[4])]
    #uvDic[tokens0[1]]=[float(tokens0[9]),float(tokens0[10])]
    #uvDic[tokens1[1]]=[float(tokens1[9]),float(tokens1[10])]
    #uvDic[tokens2[1]]=[float(tokens2[9]),float(tokens2[10])]
    i+=3
    

vertices=list(verticesDic.values())


#=======================================================================================

mesh = bpy.data.meshes.new("myBeautifulMesh")  # add the new mesh
mesh.from_pydata(vertices, [], faces)


mesh.uv_layers.new(name='NewUVMap')

bm = bmesh.new()
bm.from_mesh(mesh)
uv_layer = bm.loops.layers.uv[0]

loopIndex = 0
for face in bm.faces:
    for loop in face.loops:                     #一个三角面 = face; 每个face 有一个loops; 每个loops 有三个loop，每一个loop 对应一个vertex Index
        loop[uv_layer].uv = uvss[loopIndex]
        print(loopIndex)
        loopIndex +=1

bm.to_mesh(mesh)

#======================================================================================



obj = bpy.data.objects.new(mesh.name, mesh)
col = bpy.data.collections.get("Collection")
col.objects.link(obj)
bpy.context.view_layer.objects.active = obj
obj.select_set(True)



# Creates the path for the exported fbx.
obj_path = os.getcwd() + '//..//VOutput//' + obj.name + '.fbx' 

# Export object as fbx. Works, except all selected objects are
# exported into single fbx instead of one at a time from the list.
bpy.ops.export_scene.fbx(filepath=obj_path, use_selection=True)

# Prints each object in list.  Works.
print(obj.name)