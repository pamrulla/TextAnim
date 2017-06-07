import bpy
from math import radians
import json

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

"""     
keys_full = [
        [
            {'loc':(0, 0.2, 0), 'rot':(0, 0, 0), 'sca':(1, 1, 1), 'frame':0},
            {'loc':(2, 0.45, 0), 'rot':(0, radians(90), radians(45)), 'sca':(0.001, 0.001, 0.001), 'frame':1},
            {'loc':(0, 0.2, 0), 'rot':(0, 0, 0), 'sca':(1, 1, 1), 'frame':24},
            {'loc':(0, 0.2, 0), 'rot':(0, 0, 0), 'sca':(1, 1, 1), 'frame':72},
            {'loc':(2, 0.45, 0), 'rot':(0, radians(90), radians(45)), 'sca':(0.001, 0.001, 0.001), 'frame':96}
         ],
         [
            {'loc':(0, -1.2, 0), 'rot':(0, 0, 0), 'sca':(1, 1, 1), 'frame':0},
            {'loc':(-2, -1.45, 0), 'rot':(0, radians(-90), radians(-45)), 'sca':(0.001, 0.001, 0.001), 'frame':1},
            {'loc':(0, -1.2, 0), 'rot':(0, 0, 0), 'sca':(1, 1, 1), 'frame':24},
            {'loc':(0, -1.2, 0), 'rot':(0, 0, 0), 'sca':(1, 1, 1), 'frame':72},
            {'loc':(-2, -1.45, 0), 'rot':(0, radians(-90), radians(-45)), 'sca':(0.001, 0.001, 0.001), 'frame':96}
         ]
     ]

with open("test", 'w') as f:
    json.dump(keys_full, f)"""
keys_full = None
 
with open("test", 'r') as f:
    global keys_full
    keys_full = json.load(f)

t1 = keys_full[0]
t2 = keys_full[1]
    
def addKeyFrames(obj, dataList):
    for data in dataList:
        obj.delta_location = data['loc']
        obj.delta_rotation_euler = data['rot']
        obj.delta_scale = data['sca']
        obj.keyframe_insert(data_path="delta_location", frame=data['frame'])
        obj.keyframe_insert(data_path="delta_rotation_euler", frame=data['frame'])
        obj.keyframe_insert(data_path="delta_scale", frame=data['frame'])

def addTextObject(text):
    bpy.ops.object.text_add()
    text1 = bpy.context.active_object
    text1.data.align_x = 'CENTER'
    text1.data.body = text
    text1.name = text
    return text1
    
def addEmptyObject(text):
    bpy.ops.object.empty_add()
    empty = bpy.context.active_object
    empty.name = text
    empty.empty_draw_type = 'CIRCLE'
    empty.rotation_euler.x = radians(90)
    return empty
        
def makeParent(empty, texts):
    bpy.ops.object.select_all(action='DESELECT')
    for text in texts:
        text.select = True
    empty.select = True
    bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
    bpy.ops.object.select_all(action='DESELECT')

def setCurrentFrame():
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.scene.frame_set(1)
    
class TextAnimOne(bpy.types.Operator):
    """Creates pre-made text animations"""
    bl_idname = "text_anim.pone"
    bl_label = "Text 001"
    bl_options = {'REGISTER', 'UNDO'}
    bl_context = "objectmode"

    def execute(self, context):
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)

        text1 = addTextObject("Khan")
        
        text2 = addTextObject("Amrulla")
        
        empty = addEmptyObject("textMain")
        
        makeParent(empty, [text1, text2])

        addKeyFrames(text1, t1)
        addKeyFrames(text2, t2)
        
        setCurrentFrame()

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
    bpy.utils.unregister_module(__name__)
    
def menu_func(self, context):
    self.layout.operator(TextAnim.bl_idname, icon='MESH_CUBE')
    
if __name__ == '__main__':
    register()
