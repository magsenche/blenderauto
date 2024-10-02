import math

import bpy
from mathutils import Vector


def configure(camera_scale=15):
    # Remove all objects except base camera and light (if not hidden in viewport)
    bpy.ops.object.select_all(action="SELECT")
    bpy.data.objects["Camera"].select_set(False)
    bpy.data.objects["Light"].select_set(False)
    bpy.ops.object.delete()

    # Set up light
    light = bpy.data.objects["Light"]
    # We don't want any shadows for now
    light.data.use_shadow = False
    # SUN type generates a flat light so that there are no reflections on the objects
    light.data.type = "SUN"
    light.location = Vector((5, 0, 0))
    light.rotation_euler = Vector((0, math.radians(90), 0))

    # Set up camera
    camera = bpy.data.objects["Camera"]
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = camera_scale
    camera.location = Vector((5, 0, 0))
    camera.rotation_euler = Vector((0, math.radians(90), 0))


def import_objects(file_path):
    old_objects = set(bpy.context.scene.objects)
    bpy.ops.wm.obj_import(filepath=str(file_path))
    new_objects = set(bpy.context.scene.objects) - old_objects
    return new_objects


def render_and_save_animation(
    op,
    format,
    start=0,
    end=10,
    resolution_percentage=100,
    resolution_x=320,
    resolution_y=320,
):
    # Set up rendering
    bpy.context.scene.render.filepath = op
    bpy.context.scene.render.image_settings.file_format = format
    bpy.context.scene.render.resolution_percentage = resolution_percentage
    bpy.context.scene.render.resolution_x = resolution_x
    bpy.context.scene.render.resolution_y = resolution_y
    if format == "FFMPEG":
        bpy.context.scene.render.ffmpeg.format = "MPEG4"

    # Set up animation
    bpy.context.scene.frame_start = start
    bpy.context.scene.frame_end = end

    # Render
    bpy.ops.render.render(animation=True)
