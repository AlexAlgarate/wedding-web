from enum import Enum


class Route(Enum):
    INDEX = "/"
    CONTACT = "/contact"


class FileRoutes(Enum):
    JS_COUNTDOWN = "/js/countdown.js"
    FLAMINGO_LEFT = "/flamingo_left.png"
    FLAMINGO_RIGHT = "/flamingo_right.png"
    IMAGE_HEADER_ONE = "/vicky_bici_copia.png"
    IMAGE_HEADER_TWO = "/vicky_bota_copia.png"
    IMAGE_HOME = "/hogar.png"
    BUS = "/autobus.png"
