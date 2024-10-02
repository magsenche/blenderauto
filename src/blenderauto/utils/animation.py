import collections

import blenderauto

# Each part of the animation is a combination of one or several simple transformations
# (rotation, translation, resize, mirror) which will be executed in a certain number of frames
# A transformation is a tuple (duration, action) where:
# - duration is the number of frames of the transformation
# - action is a tuple (action_name, action_args)
# file_path is the blender object file path
Animation = collections.namedtuple("Animation", "file_path transformations")


def add(animation):
    objects = blenderauto.scene.import_objects(animation.file_path)
    obj = objects.pop()
    obj = custom(obj, animation.transformations)


def custom(object, transformations):
    step = 0
    keyframe_insert_all(object, step)
    for duration, action in transformations:
        step += duration
        blenderauto.action.apply(object, *action)
        keyframe_insert_all(object, step)
    return object


def keyframe_insert_all(moving_object, step):
    moving_object.keyframe_insert(data_path="location", frame=step)
    moving_object.keyframe_insert(data_path="rotation_euler", frame=step)
    moving_object.keyframe_insert(data_path="scale", frame=step)


def duration(transformations):
    return sum([t[0] for t in transformations])
