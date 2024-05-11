import reflex as rx

# Styles
from linktree_dai.styles.styles import Size

# Components
from linktree_dai.components.navbar.logo import logo

# State
from linktree_dai.pages.index.index_state import IndexState

def navbar() -> rx.components:
    return rx.hstack(
        logo(),
        rx.spacer(),
        rx.button(
            rx.cond(
                IndexState.light_mode,
                rx.image(
                    src='/icons/blue/sun.svg',
                    alt= 'Icono del Sol',
                    height='30px',
                ),
                rx.image(
                    src='/icons/white/moon.svg',
                    alt= 'Icono de la Luna',
                    height='30px',
                )
            ),
            style= {
                'border': f'2px solid {rx.cond(IndexState.light_mode, IndexState.accent_color, IndexState.primary_color)}',
                'border_radius': '16px',
                'cursor': 'pointer'
            },
            bg= IndexState.secondary_color,
            filter= rx.cond(
                IndexState.light_mode,
                'brightness(1)',
                'brightness(0.9)'
            ),
            _hover= {
                'filter': rx.cond(IndexState.light_mode, 'brightness(1.1)', 'brightness(1)'),
                'transition': '0.3s'
            },
            height= '40px',
            width= '40px',
            padding= '0px',
            on_click= IndexState.toggle_theme,
        ),
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