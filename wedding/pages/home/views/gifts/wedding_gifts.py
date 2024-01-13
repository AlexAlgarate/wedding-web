import reflex as rx

from wedding import utils
from wedding.components.icon_section import icon_section
from wedding.components.main_text import main_text
from wedding.components.title_section import title_section
from wedding.routes import IconRoutes as icon


def wedding_gifts() -> rx.Component:
    return rx.vstack(
        title_section("Lista de regalos"),
        icon_section(icon=icon.ICON_GIFT.value),
        main_text(utils.gift),
        main_text(utils.account_number),
    )
