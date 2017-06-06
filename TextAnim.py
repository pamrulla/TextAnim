import bpy
from bpy.props import BoolProperty, StringProperty
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

class TextAnimPropertyGroup(bpy.types.PropertyGroup):
    textAnim = BoolProperty(name="TextAnim", default=False)
    text1 = StringProperty(name="Text1", default="")
    text2 = StringProperty(name="Text1", default="")

class TextAnimOne(bpy.types.Operator):
    """Creates pre-made text animations"""
    bl_idname = "text_anim.pone"
    bl_label = "Text 001"
    bl_options = {'REGISTER', 'UNDO'}
    bl_context = "objectmode"

    def execute(self, context):
        #bpy.ops.object.select_all(action='SELECT')
        #bpy.ops.object.delete(use_global=False)

        bpy.ops.object.text_add()
        text1 = bpy.context.active_object
        text1.data.align_x = 'CENTER'
        text1.delta_location.y = text1.delta_location.y  + 0.2
        text1.data.body ="Khan"
        

        bpy.ops.object.text_add()
        text2 = bpy.context.active_object
        text2.data.align_x = 'CENTER'
        text2.delta_location.y = text1.delta_location.y  - 1.2
        text2.data.body ="Amrulla"
        
        
        bpy.ops.object.empty_add()
        empty = bpy.context.active_object
        empty.name = "textMain"
        empty.empty_draw_type = 'CIRCLE'
        empty.rotation_euler.x = radians(90)
        empty.textAnim.textAnim = True
        
        text1.name = empty.name + "_text1"
        text2.name = empty.name + "_text2"
        
        empty.textAnim.text1 = text1.name
        empty.textAnim.text2 = text2.name        
        
        bpy.ops.object.select_all(action='DESELECT')
        text1.select = True
        text2.select = True
        empty.select = True        
        bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
        bpy.ops.object.select_all(action='DESELECT')

        text1.keyframe_insert(data_path="delta_location", frame=0.0)
        text1.keyframe_insert(data_path="delta_location", frame=24.0)
        text1.keyframe_insert(data_path="delta_location", frame=72.0)
        text1.keyframe_insert(data_path="delta_rotation_euler", frame=0.0)
        text1.keyframe_insert(data_path="delta_rotation_euler", frame=24.0)
        text1.keyframe_insert(data_path="delta_rotation_euler", frame=72.0)
        text1.keyframe_insert(data_path="delta_scale", frame=0.0)
        text1.keyframe_insert(data_path="delta_scale", frame=24.0)
        text1.keyframe_insert(data_path="delta_scale", frame=72.0)

        text1.delta_location.x += 2.0
        text1.delta_location.y += 0.25
        text1.keyframe_insert(data_path="delta_location", frame=1.0)
        text1.keyframe_insert(data_path="delta_location", frame=96.0)
        text1.delta_scale = (0.001, 0.001, 0.001)
        text1.keyframe_insert(data_path="delta_scale", frame=1.0)
        text1.keyframe_insert(data_path="delta_scale", frame=96.0)
        text1.delta_rotation_euler.z = radians(45)
        text1.delta_rotation_euler.y = radians(90)
        text1.keyframe_insert(data_path="delta_rotation_euler", frame=1.0)
        text1.keyframe_insert(data_path="delta_rotation_euler", frame=96.0)

        text2.keyframe_insert(data_path="delta_location", frame=24.0)
        text2.keyframe_insert(data_path="delta_location", frame=0.0)
        text2.keyframe_insert(data_path="delta_location", frame=72.0)
        text2.keyframe_insert(data_path="delta_rotation_euler", frame=24.0)
        text2.keyframe_insert(data_path="delta_rotation_euler", frame=0.0)
        text2.keyframe_insert(data_path="delta_rotation_euler", frame=72.0)
        text2.keyframe_insert(data_path="delta_scale", frame=24.0)
        text2.keyframe_insert(data_path="delta_scale", frame=0.0)
        text2.keyframe_insert(data_path="delta_scale", frame=72.0)

        text2.delta_location.x -= 2.0
        text2.delta_location.y -= 0.25
        text2.keyframe_insert(data_path="delta_location", frame=1.0)
        text2.keyframe_insert(data_path="delta_location", frame=96.0)
        text2.delta_scale = (0.001, 0.001, 0.001)
        text2.keyframe_insert(data_path="delta_scale", frame=1.0)
        text2.keyframe_insert(data_path="delta_scale", frame=96.0)
        text2.delta_rotation_euler.z = radians(-45)
        text2.delta_rotation_euler.y = radians(-90)
        text2.keyframe_insert(data_path="delta_rotation_euler", frame=1.0)
        text2.keyframe_insert(data_path="delta_rotation_euler", frame=96.0)

        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.scene.frame_set(1)

        """
        text1.keyframe_delete(data_path="delta_location", frame=1.0)
        text1.keyframe_delete(data_path="delta_location", frame=24.0)
        text1.keyframe_delete(data_path="delta_location", frame=72.0)
        text1.keyframe_delete(data_path="delta_location", frame=96.0)
        text1.keyframe_delete(data_path="delta_rotation_euler", frame=1.0)
        text1.keyframe_delete(data_path="delta_rotation_euler", frame=24.0)
        text1.keyframe_delete(data_path="delta_rotation_euler", frame=72.0)
        text1.keyframe_delete(data_path="delta_rotation_euler", frame=96.0)
        text1.keyframe_delete(data_path="delta_scale", frame=1.0)
        text1.keyframe_delete(data_path="delta_scale", frame=24.0)
        text1.keyframe_delete(data_path="delta_scale", frame=72.0)
        text1.keyframe_delete(data_path="delta_scale", frame=96.0)
        """
        
        return {'FINISHED'}

class TextAnimOneUpdate(bpy.types.Operator):
    """Updates the animation"""
    bl_idname = "pone.update"
    bl_label = "Update"
    bl_options = {'REGISTER'}
    bl_context = "objectmode"

    def execute(self, context):
        for ob in context.active_object.children:
            if ob.name == (context.active_object.name+"_text1"):
                if context.active_object.textAnim.text1 != "":
                    ob.data.body = context.active_object.textAnim.text1
            elif ob.name == (context.active_object.name+"_text2"):
                if context.active_object.textAnim.text2 != "":
                    ob.data.body = context.active_object.textAnim.text2
        
        return {'FINISHED'}
    
class TextAnimPOne(bpy.types.Panel):
    bl_idname = "TextAnim_POne"
    bl_label = "P One"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Text Anim"
    bl_context = "objectmode"
    
    @classmethod
    def poll(cls, context):
        return (context.mode == 'OBJECT' 
        and (context.active_object is not None)
        and	(context.active_object.textAnim is not None)
        and	context.active_object.textAnim.textAnim )
    
    def draw(self, context):
        if bpy.context.active_object.textAnim.textAnim :
            anim = bpy.context.active_object.textAnim
            box = self.layout.box()
            box.label(text=bpy.context.active_object.name + " Options")
            box.prop(anim, "text1")
            box.prop(anim, "text2")
            box.operator("pone.update")
    
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
    bpy.types.Object.textAnim = bpy.props.PointerProperty(type=TextAnimPropertyGroup)

def unregister():
    bpy.utils.unregister_module(__name__)
    
def menu_func(self, context):
    self.layout.operator(TextAnim.bl_idname, icon='MESH_CUBE')
    
if __name__ == '__main__':
    register()
