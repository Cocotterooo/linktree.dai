import reflex as rx

from linktree_dai.styles.styles import Size

from linktree_dai.pages.index.index_state import IndexState

def link_buttom(data:dict) -> rx.components:
    return rx.link(
        rx.hstack(
            rx.image(
                src= rx.cond(
                    IndexState.light_mode,
                    data.dark_icon,
                    data.light_icon
                ),
                alt= rx.cond(
                    IndexState.lang_mode,
                    data.alt_es,
                    data.alt_gl
                ),
                height= '50px',
                width= '50px',
                margin_right= Size.SMALL.value,
            ),
            rx.vstack(
                rx.text(
                    rx.cond(
                        IndexState.lang_mode,
                        data.title_es,
                        data.title_gl
                    ),
                    font_size= '18px',
                    font_weight= '600',
                ),
                rx.text(
                    rx.cond(
                        IndexState.lang_mode,
                        data.description_es,
                        data.description_gl
                    ),
                    font_size= '13px',
                ),
                spacing= '0',
            ),
            rx.spacer(),
            rx.desktop_only(
                rx.image(
                    src= rx.cond(
                        IndexState.light_mode,
                        '/icons/blue/arrow_up_right.svg',
                        '/icons/white/arrow_up_right.svg'
                    ),
                    alt= rx.cond(
                        IndexState.lang_mode,
                        'Flecha inclinada hacia arrioba a la derecha (da a entender que es para acceder a la página web)',
                        'Frecha inclinada cara arriba á dereita (da a entender que é para acceder o sitio web)'
                    ),
                    class_name= 'arrow',
                ),
                padding_right= Size.SMALL.value,
            ),
            bg= IndexState.secondary_color,
            padding= Size.SMALL.value,
            border_radius= Size.DEFAULT.value,
            border= f'2px solid {IndexState.accent_color}',
            color= IndexState.primary_color,
            _hover= {
                'bg': IndexState.accent_color,
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