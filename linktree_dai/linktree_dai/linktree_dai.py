"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
# Styles:
from linktree_dai.styles.styles import STYLESHEETS, BASE_STYLE
# Page:
from linktree_dai.pages.index.index import index

app = rx.App(
    stylesheets= STYLESHEETS,
    style= BASE_STYLE
)
app.add_page(index)
