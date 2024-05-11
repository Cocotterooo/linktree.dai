import reflex as rx

from linktree_dai.components.links.link_buttom import link_buttom

from linktree_dai.data.LinkData import LinkData

from linktree_dai.styles.styles import Size

def links_column(links: list[LinkData]) -> rx.Component:
    return rx.vstack(
        *[
            link_buttom(data)
            for data in links if not data.is_social_media and data.is_active
        ],
        rx.heading(
            'Redes Sociales',
            margin_top= Size.MEDIUM.value,
        ),
        *[
            link_buttom(data)
            for data in links if data.is_social_media and data.is_active
        ],
        spacing='3',
        width='100%'
    )


