import reflex as rx

from linktree_dai.components.links.link_buttom import link_buttom

from linktree_dai.data.LinkData import LinkData


def links_column(links: list[LinkData]) -> rx.Component:
    return rx.vstack(
        *[
            link_buttom(
                data
            )
            for data in links
        ],
        spacing= '3',
        width= '100%'
    )

