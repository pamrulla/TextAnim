import bpy
from math import radians

bl_info = {
    "name": "TextAnim",
    "author": "Patan Amrulla Khan",
    "version": (0, 0, 1),
    "blender": (2, 76, 0),
    "location": "3DView -> Tools",
    "description": "Create pre-made text animations",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Animation"
}

class TextAnimOne(bpy.types.Operator):
    """Creates pre-made text animations"""
    bl_idname = "text_anim.pone"
    bl_label = "Text 001"
    bl_options = {'REGISTER', 'UNDO'}
    bl_context = "objectmode"

    def execute(self, context):
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)

        bpy.ops.object.text_add()
        text1 = bpy.context.active_object
        text1.data.align_x = 'CENTER'
        text1.location.y = text1.location.y  + 0.2
        text1.data.body ="Khan"
        text1.name = "khan"

        bpy.ops.object.text_add()
        text2 = bpy.context.active_object
        text2.data.align_x = 'CENTER'
        text2.location.y = text1.location.y  - 1.2
        text2.data.body ="Amrulla"
        text2.name = "amrulla"

        text1.keyframe_insert(data_path="location", frame=0.0)
        text1.keyframe_insert(data_path="location", frame=24.0)
        text1.keyframe_insert(data_path="location", frame=72.0)
        text1.keyframe_insert(data_path="rotation_euler", frame=0.0)
        text1.keyframe_insert(data_path="rotation_euler", frame=24.0)
        text1.keyframe_insert(data_path="rotation_euler", frame=72.0)
        text1.keyframe_insert(data_path="scale", frame=0.0)
        text1.keyframe_insert(data_path="scale", frame=24.0)
        text1.keyframe_insert(data_path="scale", frame=72.0)

        text1.location.x += 2.0
        text1.location.y += 0.25
        text1.keyframe_insert(data_path="location", frame=1.0)
        text1.keyframe_insert(data_path="location", frame=96.0)
        text1.scale = (0.001, 0.001, 0.001)
        text1.keyframe_insert(data_path="scale", frame=1.0)
        text1.keyframe_insert(data_path="scale", frame=96.0)
        text1.rotation_euler.z = radians(45)
        text1.rotation_euler.y = radians(90)
        text1.keyframe_insert(data_path="rotation_euler", frame=1.0)
        text1.keyframe_insert(data_path="rotation_euler", frame=96.0)

        text2.keyframe_insert(data_path="location", frame=24.0)
        text2.keyframe_insert(data_path="location", frame=0.0)
        text2.keyframe_insert(data_path="location", frame=72.0)
        text2.keyframe_insert(data_path="rotation_euler", frame=24.0)
        text2.keyframe_insert(data_path="rotation_euler", frame=0.0)
        text2.keyframe_insert(data_path="rotation_euler", frame=72.0)
        text2.keyframe_insert(data_path="scale", frame=24.0)
        text2.keyframe_insert(data_path="scale", frame=0.0)
        text2.keyframe_insert(data_path="scale", frame=72.0)

        text2.location.x -= 2.0
        text2.location.y -= 0.25
        text2.keyframe_insert(data_path="location", frame=1.0)
        text2.keyframe_insert(data_path="location", frame=96.0)
        text2.scale = (0.001, 0.001, 0.001)
        text2.keyframe_insert(data_path="scale", frame=1.0)
        text2.keyframe_insert(data_path="scale", frame=96.0)
        text2.rotation_euler.z = radians(-45)
        text2.rotation_euler.y = radians(-90)
        text2.keyframe_insert(data_path="rotation_euler", frame=1.0)
        text2.keyframe_insert(data_path="rotation_euler", frame=96.0)

        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.scene.frame_set(1)

        """text1.keyframe_delete(data_path="location", frame=1.0)
        text1.keyframe_delete(data_path="location", frame=24.0)
        text1.keyframe_delete(data_path="location", frame=72.0)
        text1.keyframe_delete(data_path="location", frame=96.0)
        text1.keyframe_delete(data_path="rotation_euler", frame=1.0)
        text1.keyframe_delete(data_path="rotation_euler", frame=24.0)
        text1.keyframe_delete(data_path="rotation_euler", frame=72.0)
        text1.keyframe_delete(data_path="rotation_euler", frame=96.0)
        text1.keyframe_delete(data_path="scale", frame=1.0)
        text1.keyframe_delete(data_path="scale", frame=24.0)
        text1.keyframe_delete(data_path="scale", frame=72.0)
        text1.keyframe_delete(data_path="scale", frame=96.0)
        """
        
        return {'FINISHED'}

class TextAnim(bpy.types.Panel):
    bl_idname = "OBJECT_PT_text_anim"
    bl_label = "Text Anim"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Text Anim"
    bl_context = "objectmode"
    
    def draw(self, context):
        box = self.layout.box()
        box.label(text = "Tools")
        box.operator("text_anim.pone")
        
def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.register_module(__name__)
    
def menu_func(self, context):
    self.layout.operator(TextAnim.bl_idname, icon='MESH_CUBE')
    
if __name__ == '__main__':
    register()
