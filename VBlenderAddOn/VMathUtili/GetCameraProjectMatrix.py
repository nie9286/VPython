import bpy

context = bpy.context
scene = context.scene
camera = scene.camera
render = scene.render
depsgraph = context.evaluated_depsgraph_get()
p=camera.calc_matrix_camera(depsgraph)
print(p)