import math

import bpy
from mathutils import Matrix, Vector


def apply(object, action_name, action_args):
    if action_name == "translate":
        translate(object, *action_args)
    elif action_name == "move":
        move(object, *action_args)
    elif action_name == "rotate":
        rotate(object, *action_args)
    elif action_name == "resize":
        resize(object, action_args)
    elif action_name == "rotate_translate":
        rotate_translate(object, *action_args)
    elif action_name == "rotate_move":
        rotate_move(object, *action_args)
    elif action_name == "mirror":
        mirror(object, action_args)
    elif action_name == "identity":
        identity()


def rotate(object, axis, angle):
    object.rotation_euler[axis] += math.radians(angle)


def translate(object, tx, ty, tz):
    object.location += Vector((tx, ty, tz))


def move(object, x, y, z):
    object.location += Vector((x, y, z)) - object.location


def resize(object, scale):
    object.scale *= scale


def rotate_translate(object, axis, angle, tx, ty, tz):
    rotate(object, axis, angle)
    translate(object, tx, ty, tz)


def rotate_move(object, axis, angle, x, y, z):
    rotate(object, axis, angle)
    move(object, x, y, z)


def identity():
    pass  #  Do nothing


# May find an easier way to do this..
def mirror(object, axis):
    # Select object
    bpy.ops.object.select_all(action="DESELECT")
    object.select_set(True)

    # Prepare mirror axis and matrix
    m_axis = [0, 0, 0]
    m_axis[axis] = 1
    mirror_matrix = Matrix.Scale(-1, 3, m_axis)

    # Apply mirror to local coordinates
    bpy.ops.transform.mirror(
        orient_type="LOCAL",
        orient_matrix=mirror_matrix,
        orient_matrix_type="LOCAL",
        constraint_axis=list(map(bool, m_axis)),
    )
