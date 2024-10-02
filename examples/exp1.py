import math
import os
import pathlib

import blenderauto

DATA_FOLDER = pathlib.Path(os.getenv("DATA_FOLDER"))


def main():
    blenderauto.scene.configure(camera_scale=5)  # Reset and configure scene

    object_names = [
        "triangle",
        "circle",
        "square",
        "triangle",
        "circle",
        "square",
        "triangle",
        "circle",
        "square",
        "triangle",
        "circle",
        "square",
    ]
    NO = len(object_names)  # TODO: compute 4 and 3 in init transform using NO
    NR = 64
    NC = 256

    # Generate single object animations
    for i, object_name in enumerate(object_names):
        init = [
            (0, ("resize", 0.25)),
            (0, ("rotate", (0, 45))),
            (0, ("translate", (0, 3 * (0.5 - (i // 4) / 2), 3 * (0.5 - (i % 4) / 3)))),
        ]
        rotation = [
            (NR * i, ("identity", ())),
            (NR, ("rotate", (0, 360))),
            (NR * (NO - 1 - i), ("identity", ())),
        ]
        stable = [(8, ("identity", ()))]
        circle_dance = [
            (
                1,
                (
                    "rotate_move",
                    (
                        0,
                        360 / NC,
                        0,
                        2 * math.cos((k + i * NC / NO) * 2 * math.pi / NC),
                        2 * math.sin((k + i * NC / NO) * 2 * math.pi / NC),
                    ),
                ),
            )
            for k in range(NC)
        ]
        transformations = init + rotation + stable + circle_dance
        animation = blenderauto.animation.Animation(
            DATA_FOLDER / f"objects/{object_name}.obj", transformations
        )
        animation_duration = blenderauto.animation.duration(transformations)
        blenderauto.animation.add(animation)

    # FFMPEG: video
    video_output_path = DATA_FOLDER / f"animations/exp1_{NO}/video.mp4"
    blenderauto.scene.render_and_save_animation(
        op=str(video_output_path), format="FFMPEG", end=animation_duration
    )


if __name__ == "__main__":
    main()
