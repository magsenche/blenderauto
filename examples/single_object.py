import os
import pathlib

import blenderauto

DATA_FOLDER = pathlib.Path(os.getenv("DATA_FOLDER"))


def main():
    transformations = [
        (60, ("rotate", (0, 360))),
        (60, ("rotate", (0, -360))),
        (10, ("translate", (0, 0, 2))),
        (10, ("translate", (0, 2, -2))),
        (10, ("translate", (0, -2, -2))),
        (10, ("translate", (0, -2, 2))),
        (10, ("translate", (0, 2, 2))),
        (10, ("translate", (0, 0, -2))),
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
    animation_duration = blenderauto.animation.duration(transformations)

    # Generate single object animations
    for object_name in blenderauto.OBJECTS:
        blenderauto.scene.configure()  # Reset and configure scene

        animation = blenderauto.animation.Animation(
            DATA_FOLDER / f"objects/{object_name}.obj", transformations
        )
        blenderauto.animation.add(animation)

        # FFMPEG: video
        video_output_path = DATA_FOLDER / f"animations/{object_name}/{object_name}.mp4"
        blenderauto.scene.render_and_save_animation(
            op=str(video_output_path), format="FFMPEG", end=animation_duration
        )


if __name__ == "__main__":
    main()
