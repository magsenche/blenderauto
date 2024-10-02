import os
import pathlib
import random

import bpy

import blenderauto

DATA_FOLDER = pathlib.Path(os.getenv("DATA_FOLDER"))


def main():
    random.seed(2022)  # set seed to reproduce same generated animations
    blenderauto.scene.configure()  # Reset and configure scene

    # Pacman animation
    pacman_transformations = [
        (60, ("rotate", (0, 360))),
        (60, ("rotate", (0, -360))),
        (10, ("rotate_translate", (0, 60, 0, 0, 2))),
        (10, ("rotate_translate", (0, 60, 0, 2, -2))),
        (10, ("rotate_translate", (0, 60, 0, -2, -2))),
        (10, ("rotate_translate", (0, 60, 0, -2, 2))),
        (10, ("rotate_translate", (0, 60, 0, 2, 2))),
        (10, ("rotate_translate", (0, 60, 0, 0, -2))),
        (10, ("rotate_translate", (0, -60, 0, 0, -2))),
        (10, ("rotate_translate", (0, -60, 0, -2, 2))),
        (10, ("rotate_translate", (0, -60, 0, 2, 2))),
        (10, ("rotate_translate", (0, -60, 0, 2, -2))),
        (10, ("rotate_translate", (0, -60, 0, -2, -2))),
        (10, ("rotate_translate", (0, -60, 0, 0, 2))),
    ]
    animation_duration = blenderauto.animation.duration(pacman_transformations)
    animation = blenderauto.animation.Animation(
        DATA_FOLDER / "objects/pacman.obj", pacman_transformations
    )
    blenderauto.animation.add(animation)

    # Camera live actions
    dt = 10
    camera = bpy.data.objects["Camera"]

    rotate = [("rotate", (axis, theta)) for axis in range(3) for theta in (-30, 30)]
    move = [("move", (5, y, z)) for y in (0, 4, 8) for z in (0, 4, 8)]
    actions = [("identity", ())] + rotate + move

    for i in range(animation_duration // dt):
        random_action = random.choices(
            actions, k=1, weights=[1] + [0.1] * (len(actions) - 1)
        )[0]
        blenderauto.action.apply(camera, *random_action)
        blenderauto.animation.keyframe_insert_all(camera, (i + 1) * dt)

    video_output_path = DATA_FOLDER / "animations/live_action_pacman/video.mp4"
    blenderauto.scene.render_and_save_animation(
        op=str(video_output_path), format="FFMPEG", end=animation_duration
    )


if __name__ == "__main__":
    main()
