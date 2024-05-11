import reflex as rx

from linktree_dai.styles.styles import Size
from linktree_dai.styles.colors import Color, TextColor

def link_buttom(data:dict) -> rx.components:
    return rx.link(
        rx.hstack(
            rx.image(
                src= data.dark_icon,
                alt= data.alt,
                height= '50px',
                width= '50px',
                fill= Color.PRIMARY.value
            ),
            rx.vstack(
                rx.text(
                    data.title,
                    font_size= '18px',
                    font_weight= '600',
                ),
                rx.text(
                    data.description,
                    font_size= '13px',
                ),
                spacing= '0',
            ),
            rx.spacer(),
            rx.desktop_only(
                rx.image(
                    src= '/icons/blue/arrow_up_right.svg',
                    alt= 'Flecha inclinada hacia arrioba a la derecha',
                    class_name= 'arrow',
                ),
                padding_right= Size.SMALL.value,
            ),
            bg= Color.SECONDARY.value,
            padding= Size.SMALL.value,
            border_radius= Size.DEFAULT.value,
            border= f'2px solid {Color.ACCENT.value}',
            color= TextColor.PRIMARY.value,
            _hover= {
                'bg': Color.ACCENT.value,
                'transition': '0.4s'
            },
            width= '100%',
            align= 'center'
        ),
        class_name= 'link',
        width= '100%',
        href= data.url,
        is_external= data.is_external,
    )