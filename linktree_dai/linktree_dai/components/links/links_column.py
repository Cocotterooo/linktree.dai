import reflex as rx

# Components:
from linktree_dai.components.links.link_buttom import link_buttom
# Data:
from linktree_dai.data.LinkData import LinkData
# Styles:
from linktree_dai.styles.styles import Size

def links_column(links: list[LinkData]) -> rx.Component:
    return rx.vstack(
        # GENERAL SECTION:
        *[
            link_buttom(data)
            for data in links if not data.is_social_media and not data.is_contact and data.is_active
        ],
        # SOCIAL MEDIA SECTION:
        rx.cond(
            len([data for data in links if data.is_social_media and data.is_active]) > 0,
            rx.vstack(
                rx.heading('Redes Sociales'),
                *[
                    link_buttom(data)
                    for data in links if data.is_social_media and data.is_active
                ],
                margin_top= Size.MEDIUM.value,
                width= '100%'
            )
        ),
        # CONTACT SECTION:
        rx.cond(
            len([data for data in links if data.is_contact and data.is_active]) > 0,
            rx.vstack(
                rx.heading('Contacto'),
                *[
                    link_buttom(data)
                    for data in links if data.is_contact and data.is_active
                ],
                margin_top= Size.MEDIUM.value,
                width='100%'
            )
        ),
        spacing='3',
        width='100%'
    )


