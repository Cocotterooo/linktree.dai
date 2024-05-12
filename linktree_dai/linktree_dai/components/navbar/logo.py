import reflex as rx

from linktree_dai.styles.styles import Size
from linktree_dai.styles.fonts import Font

from linktree_dai.pages.index.index_state import IndexState

def logo() -> rx.components:
    return rx.hstack(
        rx.image(
            src='/SimboloDAI.png',
            alt= rx.cond(
                IndexState.lang_mode,
                'Logotipo de la Delegación de Alumnos de Industriales',
                'Logotipo da Delegación do Alumnado de Industriais'
            ),
            height='45px'
        ),
        rx.tablet_and_desktop(
            rx.text(
                rx.cond(
                    IndexState.lang_mode,
                    'Delegación de Alumnos de Industriales',
                    'Delegación do Alumnado de Industriais'
                ),
                font_size= Size.MEDIUM.value,
                font_weight= '600',
                font_family= Font.TITLE.value,
                line_height= '25px',
                width= rx.cond(
                    IndexState.lang_mode,
                    '250px',
                    '275px'
                ),
            ),
            width='100%',
        ),
        align='center'
    )