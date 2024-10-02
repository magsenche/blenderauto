import os
import pathlib

import blenderauto

DATA_FOLDER = pathlib.Path(os.getenv("DATA_FOLDER"))


def main():
    blenderauto.scene.configure()  # Reset and configure scene

    # Pacman
    pacman_transformations = [
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
    animation_duration = blenderauto.animation.duration(pacman_transformations)
    animation = blenderauto.animation.Animation(
        DATA_FOLDER / "objects/pacman.obj", pacman_transformations
    )
    blenderauto.animation.add(animation)

    # Square
    square_transformations = [(0, ("move", (0, 4, 4)))]
    square_animation = blenderauto.animation.Animation(
        DATA_FOLDER / "objects/square.obj", square_transformations
    )
    blenderauto.animation.add(square_animation)

    # Circle
    circle_transformations = [(0, ("move", (0, -4, 4)))]
    circle_animation = blenderauto.animation.Animation(
        DATA_FOLDER / "objects/circle.obj", circle_transformations
    )
    blenderauto.animation.add(circle_animation)

    # FFMPEG: video
    video_output_path = DATA_FOLDER / "animations/pacman/video.mp4"
    blenderauto.scene.render_and_save_animation(
        op=str(video_output_path), format="FFMPEG", end=animation_duration
    )


if __name__ == "__main__":
    main()
