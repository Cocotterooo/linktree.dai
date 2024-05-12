import reflex as rx

from linktree_dai.styles.styles import Size

from linktree_dai.constants import DAI_WEB_URL, GITHUB_REPO_URL

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
                    color= IndexState.accent_color,
                ),
                rx.text(
                    ''
                ),
                color= IndexState.primary_color,
            ),
            href= DAI_WEB_URL,
            is_external=True,
            class_name='link',
        ),
        rx.link(
            rx.hstack(
                rx.image(
                    src='/icons/white/social/github.svg',
                ),
                rx.text(
                    'Delegación de Alumnos de Industriales',
                    text_align='center'
                ),
                rx.text(
                    ' v1',
                    color= IndexState.accent_color,
                ),
                color= IndexState.primary_color,
                align= 'center'
            ),
            href= GITHUB_REPO_URL,
            is_external= True,
            class_name='link'
        ),
        align= 'center',
        width= '100%',
        padding_bottom= Size.DEFAULT.value,
        padding_top= Size.LARGE.value
    )