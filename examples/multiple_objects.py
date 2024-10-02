import os
import pathlib
import random

import blenderauto

DATA_FOLDER = pathlib.Path(os.getenv("DATA_FOLDER"))


def main():
    random.seed(0)  # set seed to reproduce same generated animations

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

    # Generate multiple objects animations
    n_animations = 5
    n_objects = 3
    for _ in range(n_animations):
        blenderauto.scene.configure()  # Reset and configure scene

        # Select k objects
        object_names = random.choices(blenderauto.OBJECTS, k=n_objects)
        names = "_".join(object_names)

        for object_name in object_names:
            # Randomly shuffle transformations to create a new animation
            shuffled_tranformations = random.sample(
                transformations, k=len(transformations)
            )
            animation = blenderauto.animation.Animation(
                DATA_FOLDER / f"objects/{object_name}.obj",
                shuffled_tranformations,
            )
            blenderauto.animation.add(animation)

        # FFMPEG: video
        video_output_path = DATA_FOLDER / f"animations/{names}/video.mp4"
        blenderauto.scene.render_and_save_animation(
            op=str(video_output_path), format="FFMPEG", end=animation_duration
        )


if __name__ == "__main__":
    main()
