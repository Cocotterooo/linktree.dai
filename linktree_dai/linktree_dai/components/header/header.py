import reflex as rx

from linktree_dai.styles.styles import Size

from linktree_dai.components.header.links_icons import links

# State
from linktree_dai.pages.index.index_state import IndexState


def header():
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src='/dai.webp',
                size='8',
                border_radius='100%',
                border= f'4px solid {IndexState.accent_color}',
            ),
            rx.vstack(
                rx.heading(
                    rx.cond(
                        IndexState.lang_mode,
                        'Delegación de Alumnos de Industriales',
                        'Delegación do Alumnado de Industriais'
                    )
                ),
                rx.text(
                    '@dai_uvigo',
                    font_weight= '300',
                    color= IndexState.accent_color,
                    size= '4',
                ),
                rx.tablet_and_desktop(
                    links(),
                ),
                padding_left= Size.DEFAULT.value,
            ),
            align= 'center'
        ),
        rx.mobile_only(
            rx.hstack(
                links(),
                justify_content='center',
                width='100%'
            ),
            width='100%'
        ),
        rx.text(
            rx.cond(
                IndexState.lang_mode,
                '''La Delegación de Alumnos es el máximo órgano de representación
                estudiantil de la Escuela de Ingeniería Industrial. Somos un órgano
                oficial de la Universidad de Vigo formado por estudiantes.''',
                '''A delegación de estudantes é o máximo órgano de representación
                estudantil da Escola de Enxeñaría Industrial. Somos un órgano
                oficial da Universidade de Vigo formado por estudantes.''',
            )
        ),
        padding_y= Size.MEDIUM_BIG.value,
    )