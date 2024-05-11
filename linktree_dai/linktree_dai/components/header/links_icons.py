import reflex as rx

from linktree_dai.components.header.link_icon import link_icon

from linktree_dai.constants import DAI_INSTAGRAM_URL, DAI_TWITTER_URL, DAI_MAIL_URL, DAI_WHATSAPP_URL, DAI_WEB_URL

def links() -> rx.components:
    return rx.hstack(
        link_icon(
            light_icon= '/icons/white/social/instagram.svg',
            dark_icon= '/icons/blue/social/instagram.svg',
            alt= 'Icono de Instagram',
            href= DAI_INSTAGRAM_URL
        ),
        link_icon(
            light_icon= '/icons/white/social/x.svg',
            dark_icon= '/icons/blue/social/x.svg',
            alt= 'Icono de Twitter / X',
            href= DAI_TWITTER_URL
        ),
        link_icon(
            light_icon= '/icons/white/social/email.svg',
            dark_icon= '/icons/blue/social/email.svg',
            alt= 'Icono de email',
            href= DAI_MAIL_URL
        ),
        link_icon(
            light_icon= '/icons/white/social/whatsapp.svg',
            dark_icon= '/icons/blue/social/whatsapp.svg',
            alt= 'Icono de whatsapp',
            href= DAI_WHATSAPP_URL
        ),
        link_icon(
            light_icon= '/icons/white/social/web.svg',
            dark_icon= '/icons/blue/social/web.svg',
            alt= 'Icono de web',
            href= DAI_WEB_URL
        )
    )