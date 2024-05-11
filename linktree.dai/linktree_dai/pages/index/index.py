import reflex as rx
# Components:
from linktree_dai.components.navbar.navbar import navbar
from linktree_dai.components.header.header import header
from linktree_dai.components.footer.footer import footer
from linktree_dai.components.links.link_buttom import link_buttom
from linktree_dai.components.links.links_column import links_column
# Utils:
from utils import INDEX_TITLE, INDEX_DESCRIPTION, PREVIEW
# Styles:
from linktree_dai.styles.styles import Size

from linktree_dai.data.LinkData import links_references
# State:
#from linktree_dai.pages.index.index_state import IndexState

#rx.foreach(MyState.items, item_component)

@rx.page(
    title=INDEX_TITLE,
    description=INDEX_DESCRIPTION,
    image=PREVIEW,
    #on_load=[IndexState]
)
def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links_column(links_references),
                footer(),
                max_width='650px',
                padding_x=Size.MEDIUM_BIG.value,
            )
        ),
        style={
            "background_image": "url('/Tema_claro.png')",
            "background_size": "cover",
            "background_repeat": "no-repeat",
            "background_attachment": "fixed",
            'background_position':['center', 'center', 'center', 'center', 'center'],
            "width": "100%",
            "height": "100%",
            "min_height": "100vh",
        }
    )