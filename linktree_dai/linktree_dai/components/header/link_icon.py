import reflex as rx

from linktree_dai.styles.styles import Size
from linktree_dai.styles.colors import Color
from linktree_dai.components.motion.motion import motion

from linktree_dai.pages.index.index_state import IndexState

def link_icon(*, light_icon: str, dark_icon, alt:str, href: str, is_external: bool = True) -> rx.components: 
    return rx.link(
        motion(
            rx.image(
                src= rx.cond(
                    IndexState.light_mode,
                    dark_icon,
                    light_icon
                ),
                alt= alt,
                height= '17px',
                width= '17px',
                padding_right= Size.DEFAULT.value,
            ),
            while_hover={"scale": 1.2},
            transition={"duration": 0.2},
            border_radius= '50%',
            bg= IndexState.primary_color,
            padding= Size.SMALL.value,
            _hover= {
                'bg': Color.ACCENT.value,
                'transition': '0.35s',
            },
        ),
        href= href,
        is_external= is_external,
        class_name= 'link',
    )