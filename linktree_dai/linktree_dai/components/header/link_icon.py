import reflex as rx

from linktree_dai.styles.styles import Size
from linktree_dai.styles.colors import Color
from linktree_dai.components.motion.motion import motion

def link_icon(*, icon: str, alt:str, href: str, is_external: bool = True) -> rx.components: 
    return rx.link(
        motion(
            rx.image(
                src= icon,
                alt= alt,
                height= '20px',
                width= '20px',
            ),
            while_hover={"scale": 1.1},
            transition={"duration": 0.2},
        ),
        border_radius= '50%',
        bg=Color.PRIMARY.value,
        padding= Size.SMALL.value,
        _hover= {
            'bg': Color.ACCENT.value,
            'transition': '0.35s',
        },
        href= href,
        is_external= is_external,
        class_name= 'link',
    )