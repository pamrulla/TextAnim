import bpy
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

styles_enum = [("0", "Anim One", "This is style one"),
    ("1", "Two One", "This is style one")]

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
keys_full = [
    [
        [
            {'loc':( 0, 0.85, 0), 'rot':( 0, 0, 0), 'sca':( 1, 1, 1), 'frame':0},
            {'loc':( 0, 0.6, 0), 'rot':( -180, 0, 0), 'sca':( 1, 0.001, 1), 'frame':1},
            {'rot':( -180, 0, 0), 'sca':( 1, 1, 1), 'frame':5},
            {'loc':( 0, 0.6, 0), 'rot':( 0, 0, 0), 'frame':15},
            {'loc':( 0, 0.43, 0), 'frame':20},
            {'loc':( 0, 0.43, 0), 'frame':25},
            {'loc':( 0, 0.85, 0), 'rot':( 0, 0, 0), 'sca':( 1, 1, 1), 'frame':31},
            {'loc':( 0, 1, 0), 'frame':40},
            {'loc':( 0, 1, 0), 'rot':( 0, 0, 0), 'sca':( 1, 1, 1), 'frame':43},
            {'loc':( 0, 0.85, 0), 'frame':55},
            {'loc':( 0, 0.85, 0), 'frame':85},
            {'loc':( 0, 1, 0), 'frame':97},
            {'loc':( 0, 1, 0), 'frame':101},
            {'loc':( 0, 0.43, 0), 'frame':121},
            {'loc':( 0, 0.6, 0), 'rot':( 0, 0, 0), 'frame':127},
            {'loc':( 0, 0.85, 0), 'rot':( -180, 0, 0), 'sca':( 1, 1, 1), 'frame':132},
            {'sca':( 1, 0.001, 1), 'frame':136}
        ],
        [
            {'loc':( 0, 0, 0), 'rot':( 0, 0, 0), 'sca':( 1, 1, 1), 'frame':0},
            {'loc':( 0, 0, 0), 'rot':( -180, 0, 0), 'sca':( 1, 0.001, 1), 'frame':1},
            {'sca':( 1, 0.001, 1), 'frame':20},
            {'rot':( -180, 0, 0), 'sca':( 1, 0.001, 1), 'frame':25},
            {'rot':( -180, 0, 0), 'sca':( 1, 1, 1), 'frame':31},
            {'rot':( 0, 0, 0), 'sca':( 1.5, 1.5, 1), 'frame':40},
            {'loc':( 0, 0, 0), 'rot':( 0, 0, 0), 'sca':( 1.5, 1.5, 1), 'frame':43},
            {'sca':( 1, 1, 1), 'frame':55},
            {'sca':( 1, 1, 1), 'frame':85},
            {'sca':( 1.5, 1.5, 1), 'frame':97},
            {'rot':( 0, 0, 0), 'sca':( 1.5, 1.5, 1), 'frame':101},
            {'rot':( -180, 0, 0), 'sca':( 1, 1, 1), 'frame':110},
            {'sca':( 1, 0.001, 1), 'frame':116},
        ],
        [
            {'loc':( 0, -0.85, 0), 'rot':( 0, 0, 0), 'sca':( 1, 1, 1), 'frame':0},
            {'loc':( 0, -0.6, 0), 'rot':( -180, 0, 0), 'sca':( 1, 0.001, 1), 'frame':1},
            {'rot':( -180, 0, 0), 'sca':( 1, 1, 1), 'frame':5},
            {'loc':( 0, -0.6, 0), 'rot':( 0, 0, 0), 'frame':15},
            {'loc':( 0, -0.43, 0), 'frame':20},
            {'loc':( 0, -0.43, 0), 'frame':25},
            {'loc':( 0, -0.85, 0), 'rot':( 0, 0, 0), 'sca':( 1, 1, 1), 'frame':31},
            {'loc':( 0, -1, 0), 'frame':40},
            {'loc':( 0, -1, 0), 'rot':( 0, 0, 0), 'sca':( 1, 1, 1), 'frame':43},
            {'loc':( 0, -0.85, 0), 'frame':55},
            {'loc':( 0, -0.85, 0), 'frame':85},
            {'loc':( 0, -1, 0), 'frame':97},
            {'loc':( 0, -1, 0), 'frame':101},
            {'loc':( 0, -0.43, 0), 'frame':121},
            {'loc':( 0, -0.6, 0), 'rot':( 0, 0, 0), 'frame':127},
            {'loc':( 0, -0.85, 0), 'rot':( -180, 0, 0), 'sca':( 1, 1, 1), 'frame':132},
            {'sca':( 1, 0.001, 1), 'frame':136}
        ]
    ]
]

"""with open("test", 'w') as f:
    json.dump(keys_full, f)
keys_full = None
 
with open("test", 'r') as f:
    global keys_full
    keys_full = json.load(f)"""

def addKeyFrames(obj, dataList):
    for data in dataList:
        if 'loc' in data:
            obj.delta_location = data['loc']
        if 'rot' in data:
            obj.delta_rotation_euler.x = radians(data['rot'][0])
            obj.delta_rotation_euler.y = radians(data['rot'][1])
            obj.delta_rotation_euler.z = radians(data['rot'][2])
        if 'sca' in data:
            obj.delta_scale = data['sca']
        obj.keyframe_insert(data_path="delta_location", frame=data['frame'])
        obj.keyframe_insert(data_path="delta_rotation_euler", frame=data['frame'])
        obj.keyframe_insert(data_path="delta_scale", frame=data['frame'])

def addTextObject(text):
    bpy.ops.object.text_add()
    text1 = bpy.context.active_object
    text1.data.align_x = 'CENTER'
    text1.data.body = text
    text1.data.extrude = 0.001
    text1.name = text
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    return text1
    
def addEmptyObject(text):
    bpy.ops.object.empty_add()
    empty = bpy.context.active_object
    empty.name = text
    empty.empty_draw_type = 'CIRCLE'
    empty.rotation_euler.x = radians(90)
    #empty.textAnim.textAnim = True
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
        if context.scene.selectionTextAnimStyle == "0":
            bpy.ops.object.select_all(action='SELECT')
            bpy.ops.object.delete(use_global=False)

            text_objs = []
            
            i = 1
            for data in keys_full[int(context.scene.selectionTextAnimStyle)]:
                text_objs.append(addTextObject('text'+str(i)))
                addKeyFrames(text_objs[i-1], data)
                i += 1
            
            empty = addEmptyObject("AnimMain " + context.scene.selectionTextAnimStyle)
            
            makeParent(empty, text_objs)
            
            setCurrentFrame()
        
        return {'FINISHED'}

"""
class TextAnimPropertyGroup(bpy.types.PropertyGroup):
    textAnim = BoolProperty(name="TextAnim", default=False)
    text1 = StringProperty(name="Text1", default="")
    text2 = StringProperty(name="Text1", default="")

class TextAnimOneUpdate(bpy.types.Operator):
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
"""
    
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
    #bpy.types.Object.textAnim = bpy.props.PointerProperty(type=TextAnimPropertyGroup)

def unregister():
    bpy.utils.unregister_module(__name__)
    
def menu_func(self, context):
    self.layout.operator(TextAnim.bl_idname, icon='MESH_CUBE')
    
if __name__ == '__main__':
    register()
