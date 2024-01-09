from enum import Enum


class Font(Enum):
    DEFAULT = "Antic Didone"
    TITLE = "Alex Brush"


class FontWeight(Enum):
    LIGHT = "300"
    MEDIUM = "500"
    BOLD = "800"


class FontHeight(Enum):
    SMALL = "0.5em"
    DEFAULT = "1em"
    MEDIUM = "1.25em"
    BIG = "2em"
