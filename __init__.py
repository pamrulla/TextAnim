import bpy
import os
import json
from bpy.props import BoolProperty, StringProperty, EnumProperty
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

styles_enum = []

dataFilesLocation = os.path.join(os.path.dirname(__file__), "d")
filesList = os.listdir(dataFilesLocation)
filesList.sort(key= int)

for fl in filesList:
    with open(os.path.join(dataFilesLocation, fl), 'r') as f:
        content = json.load(f)
        styles_enum.append((content['index'], content['name'], content['desc']))

bpy.types.Scene.selectionTextAnimStyle = EnumProperty(
        items=styles_enum,
        name="Animation Types")

"""keys_full = [
        [
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
     ]"""

def addKeyFrames(obj, dataList):
    for data in dataList:
        if 'loc' in data:
            obj.delta_location = data['loc']
            obj.keyframe_insert(data_path="delta_location", frame=data['frame'])
        
        if 'rot' in data:
            obj.delta_rotation_euler.x = radians(data['rot'][0])
            obj.delta_rotation_euler.y = radians(data['rot'][1])
            obj.delta_rotation_euler.z = radians(data['rot'][2])
            obj.keyframe_insert(data_path="delta_rotation_euler", frame=data['frame'])
        
        if 'sca' in data:
            obj.delta_scale = data['sca']
            obj.keyframe_insert(data_path="delta_scale", frame=data['frame'])

def addTextObject(text):
    bpy.ops.object.text_add()
    text1 = bpy.context.active_object
    text1.data.align_x = 'CENTER'
    text1.data.body = text
    text1.data.extrude = 0.001
    text1.name = "AnimMain" + bpy.context.scene.selectionTextAnimStyle + '_' + text
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    return text1
    
def addEmptyObject(text):
    bpy.ops.object.empty_add()
    empty = bpy.context.active_object
    empty.name = text
    empty.empty_draw_type = 'CIRCLE'
    empty.rotation_euler.x = radians(90)
    empty.textAnim.textAnim = True
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

class TextAnimCreate(bpy.types.Operator):
    """Creates pre-made text animations"""
    bl_idname = "text_anim.create"
    bl_label = "Create"
    bl_options = {'REGISTER', 'UNDO'}
    bl_context = "objectmode"

    def execute(self, context):
        #bpy.ops.object.select_all(action='SELECT')
        #bpy.ops.object.delete(use_global=False)

        text_objs = []
        
        i = 1
        
        with open(os.path.join(dataFilesLocation, context.scene.selectionTextAnimStyle), 'r') as f:
            content = json.load(f)
            for data in content['data']:
                text_objs.append(addTextObject('Text' + str(i)))
                addKeyFrames(text_objs[i-1], data)
                i += 1
        
        empty = addEmptyObject("AnimMain" + context.scene.selectionTextAnimStyle)
        
        makeParent(empty, text_objs)
        
        setCurrentFrame()
        
        return {'FINISHED'}

class TextAnimPropertyGroup(bpy.types.PropertyGroup):
    textAnim = BoolProperty(name="TextAnim", default=False)
    text1 = StringProperty(name="Text1", default="")
    text2 = StringProperty(name="Text1", default="")
    text3 = StringProperty(name="Text3", default="")

class TextAnimOUpdate(bpy.types.Operator):
    bl_idname = "textanim.update"
    bl_label = "Update"
    bl_options = {'REGISTER'}
    bl_context = "objectmode"

    def execute(self, context):
        for ob in context.active_object.children:
            if "_Text1" in ob.name:
                if context.active_object.textAnim.text1 != "":
                    ob.data.body = context.active_object.textAnim.text1
            elif "_Text2" in ob.name:
                if context.active_object.textAnim.text2 != "":
                    ob.data.body = context.active_object.textAnim.text2
            elif "_Text3" in ob.name:
                if context.active_object.textAnim.text3 != "":
                    ob.data.body = context.active_object.textAnim.text3
            
        return {'FINISHED'}
    
class TextAnimControllerPanel(bpy.types.Panel):
    bl_idname = "TextAnim.ControllerPanel"
    bl_label = "Controller Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Text Anim"
    bl_context = "objectmode"
    
    @classmethod
    def poll(cls, context):
        return (context.mode == 'OBJECT' 
        and (context.active_object is not None)
        and    (context.active_object.textAnim is not None)
        and    context.active_object.textAnim.textAnim )
    
    def draw(self, context):
        if bpy.context.active_object.textAnim.textAnim :
            anim = bpy.context.active_object.textAnim
            box = self.layout.box()
            box.label(text=bpy.context.active_object.name + " Options")
            i = 1
            while i <= len(bpy.context.active_object.children):
                box.prop(anim, "text" + str(i))
                i += 1
            box.operator("textanim.update")
    
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
        box.prop(context.scene, 'selectionTextAnimStyle')
        box.operator("text_anim.create")
        
def register():
    bpy.utils.register_module(__name__)
    bpy.types.Object.textAnim = bpy.props.PointerProperty(type=TextAnimPropertyGroup)

def unregister():
    bpy.utils.unregister_module(__name__)
    
def menu_func(self, context):
    self.layout.operator(TextAnim.bl_idname, icon='MESH_CUBE')
    
if __name__ == '__main__':
    register()
