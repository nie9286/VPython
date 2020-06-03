import bpy
import math
import random

radians = math.radians(90)

rangeP = 5
xp = (random.random() * 2 -1) * rangeP
yp = (random.random() * 2 -1) * rangeP

xr = random.random()
xr *= 360
xr = math.radians(xr)

bpy.ops.mesh.primitive_plane_add(size=1, enter_editmode=False, location=(xp,yp,0.5),rotation=(xr,radians,0))