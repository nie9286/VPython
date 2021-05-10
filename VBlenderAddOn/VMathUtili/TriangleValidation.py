import mathutils 
from mathutils import *


Vector = mathutils.Vector

v1 = mathutils.Vector((1,0,0))
v2 = mathutils.Vector((0,1,0))
v3 = mathutils.Vector((1,10,0))

area = mathutils.geometry.area_tri(v1,v2,v3)

print(area)