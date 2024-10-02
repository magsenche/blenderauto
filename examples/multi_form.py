import os
import pathlib
import random

import blenderauto

DATA_FOLDER = pathlib.Path(os.getenv("DATA_FOLDER"))


def main():
    random.seed(0)  # set seed to reproduce same generated animations
    # Create test dataset with multiple shapes moving around
    shapes_triplets = [
        ("shoe", "triangle", "pacman", False),
        ("shoe", "triangle", "pacman", True),
        ("shoe", "square", "pacman", False),
        ("shoe", "square", "pacman", True),
    ]
    for e in shapes_triplets:
        many_shapes(*e)


def many_shapes(main_shape, other_shape_1, other_shape_2, do_superpose):
    my, mz = (0, 0) if do_superpose else (3, 3)
    ty, tz = (1, 1) if do_superpose else (0.5, 0.5)
    name = f"{main_shape}_{other_shape_1}_{other_shape_2}_{do_superpose}"
    blenderauto.scene.configure()  # Reset and configure scene

    # main_shape
    resize = [(0, ("resize", 1.0))]
    transformations = [
        (30, ("rotate", (0, 360))),
        (30, ("rotate", (0, -360))),
        (10, ("translate", (0, 0, tz))),
        (10, ("translate", (0, ty, -tz))),
        (10, ("translate", (0, -ty, -tz))),
        (10, ("translate", (0, -ty, tz))),
        (10, ("translate", (0, ty, tz))),
        (10, ("translate", (0, 0, -tz))),
        (10, ("rotate_translate", (0, 60, 0, 0, tz))),
        (10, ("rotate_translate", (0, 60, 0, ty, -tz))),
        (10, ("rotate_translate", (0, 60, 0, -ty, -tz))),
        (10, ("rotate_translate", (0, 60, 0, -ty, tz))),
        (10, ("rotate_translate", (0, 60, 0, ty, tz))),
        (10, ("rotate_translate", (0, 60, 0, 0, -tz))),
        (10, ("rotate_translate", (0, -60, 0, 0, -tz))),
        (10, ("rotate_translate", (0, -60, 0, -ty, tz))),
        (10, ("rotate_translate", (0, -60, 0, ty, tz))),
        (10, ("rotate_translate", (0, -60, 0, ty, -tz))),
        (10, ("rotate_translate", (0, -60, 0, -ty, -tz))),
        (10, ("rotate_translate", (0, -60, 0, 0, tz))),
    ]
    animation_duration = blenderauto.animation.duration(transformations)

    # main_shape
    main_shape_transformations = (
        resize
        + [(0, ("move", (0, 0, -mz)))]
        + random.sample(transformations, k=len(transformations))
    )
    animation = blenderauto.animation.Animation(
        DATA_FOLDER / f"objects/{main_shape}.obj", main_shape_transformations
    )
    blenderauto.animation.add(animation)

    # other_shape_1
    other_shape_1_transformations = (
        resize
        + [(0, ("move", (0, my, mz)))]
        + random.sample(transformations, k=len(transformations))
    )
    other_shape_1_animation = blenderauto.animation.Animation(
        DATA_FOLDER / f"objects/{other_shape_1}.obj",
        other_shape_1_transformations,
    )
    blenderauto.animation.add(other_shape_1_animation)

    # other_shape_2
    other_shape_2_transformations = (
        resize
        + [(0, ("move", (0, -my, mz)))]
        + random.sample(transformations, k=len(transformations))
    )
    other_shape_2_animation = blenderauto.animation.Animation(
        DATA_FOLDER / f"objects/{other_shape_2}.obj",
        other_shape_2_transformations,
    )
    blenderauto.animation.add(other_shape_2_animation)

    destination = DATA_FOLDER / "animations" / "multi_shape"

    # FFMPEG: video
    video_output_path = destination / name / f"video.mp4"
    blenderauto.scene.render_and_save_animation(
        op=str(video_output_path), format="FFMPEG", end=animation_duration
    )


if __name__ == "__main__":
    main()
