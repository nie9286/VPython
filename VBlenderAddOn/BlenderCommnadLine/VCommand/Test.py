import bpy 
import math 
from mathutils import Matrix
import os

def vert(x,y,z):
    """ Make a vertex """
    return (x, y, z)

verts = []
faces = [] 

name = 'Cubert'

mesh = bpy.data.meshes.new(name)
mesh.from_pydata(verts, [], faces)

obj = bpy.data.objects.new(name, mesh)
bpy.context.scene.collection.objects.link(obj)

bpy.context.view_layer.objects.active = obj

# Creates the path for the exported fbx.
obj_path = os.getcwd() + '//VOutput//' + obj.name + '.fbx' 

# Export object as fbx. Works, except all selected objects are
# exported into single fbx instead of one at a time from the list.
bpy.ops.export_scene.fbx(filepath=obj_path, use_selection=True)

# Prints each object in list.  Works.
print(obj.name)