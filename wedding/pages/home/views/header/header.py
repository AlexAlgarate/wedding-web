import reflex as rx

import wedding.utils as utils

from .components import (
    image_header,
    title_header,
    wedding_date_header,
    wedding_hour_header,
)


def header() -> rx.Component:
    """
    Creates a header component with title, image, and wedding date.

    Returns:
        rx.Component: The header component.
    """

    return rx.vstack(
        rx.flex(
            title_header(),
            image_header(),
            wedding_date_header(list_date=utils.wedding_date, size="2xl"),
            wedding_hour_header(hour="18:30", size="xl"),
            direction="column",
            align_items="center",
            align_self="stretch",
            gap="8px",
        ),
        id="header_section",
    )
