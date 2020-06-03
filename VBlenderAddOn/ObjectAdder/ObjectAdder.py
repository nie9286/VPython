bl_info={
    "name" : "Object Adder",
    "author" : "Visin",
    "version" : (1,0),
    "blender" : (2,80,0),
    "location" : "View3D > Tool",
    "category" : "Add Mesh",
}



import bpy


#region Classes

class TestPanel(bpy.types.Panel):
    bl_idname = "TestPanel"
    bl_label = "PT_TestPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "NewTab"
    

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text="Add an object",icon="CUBE")
        row = layout.row()
        row.operator("mesh.primitive_cube_add",icon="CUBE")
        row = layout.row()
        row.operator("mesh.primitive_uv_sphere_add",icon="SPHERE")
        
        
class PanelA(bpy.types.Panel):
    bl_idname = "Test A"
    bl_label = "PT_PanelA"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PanelA"
    bl_parent_id = "TestPanel"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        row = layout.row()
        row.label(text="Selecet an option to scale your object.", icon="VIEW_ZOOM")
        row = layout.row()
        row.operator("transform.resize")
        row = layout.row()
        row.prop(obj,"scale")
        
        
        
        
        
class PanelB(bpy.types.Panel):
    bl_idname = "Test B"
    bl_label = "PT_PanelB"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PanelB"
    bl_parent_id = "TestPanel"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text="Select a Special Option",icon="VIEW_ZOOM")
        row = layout.row()
        row.operator("object.shade_smooth",icon="MOD_SMOOTH",text="Set Smooth Shading")
        row = layout.row()
        row.operator("object.subdivision_set")
        row = layout.row()
        row.operator("object.modifier_add")
        
        
        
#endregion


def register():
    bpy.utils.register_class(TestPanel)
    bpy.utils.register_class(PanelA)
    bpy.utils.register_class(PanelB)


def unregister():
    bpy.utils.unregister_class(TestPanel)
    bpy.utils.unregister_class(PanelA)
    bpy.utils.unregister_class(PanelB)

if __name__ == "__main__":
    register()