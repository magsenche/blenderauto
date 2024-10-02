import datetime

from blenderauto.utils import action, animation, bnw, scene


def get_version() -> str:
    return datetime.datetime.now().strftime("%Y.%m.%d")


OBJECTS = [
    "batman",
    "bowl",
    "circle",
    "complex_shape",
    "cube",
    "decagon",
    "heptagon",
    "hexagon",
    "nonagon",
    "octogon",
    "pacman",
    "pentagon",
    "shoe",
    "square",
    "star",
    "torus",
    "triangle",
]
