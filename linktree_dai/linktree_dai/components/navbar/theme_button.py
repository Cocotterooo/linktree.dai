import reflex as rx

from linktree_dai.pages.index.index_state import IndexState

def theme_button():
    return rx.button(
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
    )