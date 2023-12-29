from simple_chat import styles
from simple_chat.components import chat, navbar, sidebar
from simple_chat.templates import template

import nextpy as xt

@template(route='/nextpy_gpt', title="NextpyGPT")
def nextpy_gpt() -> xt.Component:
    """The main app."""
    return xt.vstack(
        navbar(),
        xt.vstack(
            chat.chat(),
            chat.action_bar(),
            width = "92%",
            align_self = "center",
            bg=styles.border_color,
            min_h="100vh",
            class_name = "rounded-md"
        ),
        sidebar(),
        bg=styles.bg_dark_color,
        color=styles.text_light_color,
        min_h="100vh",
        spacing="0",
    )
