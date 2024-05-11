import reflex as rx

# Styles
from linktree_dai.styles.styles import Size
from linktree_dai.styles.colors import Color, TextColor
from linktree_dai.styles.fonts import Font, FontWeight

# Components
from linktree_dai.components.navbar.logo import logo

def navbar() -> rx.components:
    return rx.hstack(
        logo(),
        rx.spacer(),
        rx.image(
            src='/EEI-logo.svg',
            alt= 'Logotipo de la Escuela de Ingeniería Industrial de la Universidad de Vigo',
            height='50px',
        ),
        align='center',
        border_top= f'1px solid {Color.ACCENT.value}',
        style= {
            'bg': f'{Color.SECONDARY.value}F2', # 0.85 opacity
            'backdrop-filter': 'blur(15px)',
        },
        position= 'sticky',
        z_index= '999',
        top= '0',
        width='100%',
        padding_x= Size.MEDIUM_BIG.value,
        padding_y= Size.SMALL.value
    )