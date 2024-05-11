import reflex as rx

from linktree_dai.styles.styles import Size
from linktree_dai.styles.colors import TextColor
from linktree_dai.styles.fonts import Font, FontWeight

from linktree_dai.constants import DAI_WEB_URL

from linktree_dai.pages.index.index_state import IndexState

def footer():
    return rx.vstack(
        rx.image(
            src='/SimboloDAI.png',
            height='45px',
        ),
        rx.link(
            rx.hstack(
                rx.text(
                    '© 2024 DAI -'
                ),
                rx.text(
                    ' Universidade de Vigo ',
                    color= TextColor.ACCENT.value,
                ),
                rx.text(
                    '- v1'
                ),
                color= IndexState.primary_color,
            ),
            href= DAI_WEB_URL,
            is_external=True,
            class_name='link',
        ),
        align='center',
        width='100%',
        padding_bottom= Size.DEFAULT.value,
        padding_top= Size.LARGE.value,
    )