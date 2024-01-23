import reflex as rx

from wedding import urls, utils
from wedding.components import (
    button,
    card,
    divider,
    icon_section,
    text_paragraph,
    title_section,
)
from wedding.routes import IconRoutes as icon


def wedding_google_photos() -> rx.Component:
    return card(
        icon_section(icon=icon.ICON_CAMERA.value),
        title_section(title=utils.title_photo),
        divider(width="50%", section=False),
        text_paragraph(text=utils.google_photo_text_one),
        text_paragraph(text=utils.google_photo_text_two),
        button(button_name=utils.google_photo_button, url=urls.GOOGLE_FOTOS_URL),
    )
