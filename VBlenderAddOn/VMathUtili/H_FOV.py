import bpy
import math

context = bpy.context
scene = context.scene
camera = scene.camera

hfov = math.degrees(2 * math.atan(camera.data.sensor_width /(2 * camera.data.lens)))
vfoc = math.degrees(2 * math.atan(camera.data.sensor_height /(2 * camera.data.lens)))
print("Horizatal FOV : " + str(hfov))
print("Vertical FOV : " + str(vfoc))