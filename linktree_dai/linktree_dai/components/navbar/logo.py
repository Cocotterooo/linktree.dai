import reflex as rx

from linktree_dai.styles.styles import Size
from linktree_dai.styles.fonts import Font
from linktree_dai.styles.colors import TextColor

def logo() -> rx.components:
    return rx.hstack(
        rx.image(
            src='/SimboloDAI.png',
            alt= 'Logotipo de la Delegación de Alumnos de Industriales',
            height='45px',
        ),
        rx.tablet_and_desktop(
            rx.text(
                'Delegación de Alumnos de Industriales',
                font_size= Size.MEDIUM.value,
                font_weight= '600',
                font_family= Font.TITLE.value,
                line_height= '25px',
                width= '250px'
            ),
            width='100%',
        ),
        align='center'
    )