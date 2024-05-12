import reflex as rx

from linktree_dai.pages.index.index_state import IndexState


def language_button():
    return rx.button(
        rx.image(
            src= rx.cond(
                IndexState.lang_mode, 
                '/icons/flags/spain.svg',
                '/icons/flags/galicia.svg'
            ),
            alt= rx.cond(
                IndexState.lang_mode, 
                'Icono de la bandera de España', 
                'Icono da bandeira de Galicia'
            ),
            height='30px',
            border_radius='100%'
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
        box_shadow= '0 0 5px rgba(0,0,0,0.25)',
        on_click= IndexState.toggle_language,
    )