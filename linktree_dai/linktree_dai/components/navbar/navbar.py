import reflex as rx

# Styles
from linktree_dai.styles.styles import Size

# Components
from linktree_dai.components.navbar.logo import logo
from linktree_dai.components.navbar.theme_button import theme_button
from linktree_dai.components.navbar.language_button import language_button

# State
from linktree_dai.pages.index.index_state import IndexState


def navbar() -> rx.components:
    return rx.hstack(
        logo(),
        rx.spacer(),
        theme_button(),
        language_button(),
        rx.image(
            src='/EEI-logo.svg',
            alt= 'Logotipo de la Escuela de Ingeniería Industrial de la Universidad de Vigo',
            height='50px',
        ),
        align='center',
        border_top= f'1px solid {IndexState.accent_color}',
        style= {
            'bg': f'{IndexState.secondary_color}F2', # 0.85 opacity
            'backdrop-filter': 'blur(20px)',
            'position': 'sticky',
            'z_index': '999',
            'top': '0',
            'width':'100%',
            'padding_x': Size.MEDIUM_BIG.value,
            'padding_y': Size.SMALL.value
        }
    )