import json

class LinkData:
    def __init__(
            self,
            title_es: str,
            title_gl: str,
            description_es: str,
            description_gl: str,
            light_icon: str,
            dark_icon: str,
            alt_es: str,
            alt_gl: str,
            url: str,
            is_external: bool,
            is_social_media: bool = False,
            is_contact: bool = False,
            is_active: bool = False
        ):
        self.title_es = title_es
        self.title_gl = title_gl
        self.description_es = description_es
        self.description_gl = description_gl
        self.light_icon = light_icon
        self.dark_icon = dark_icon
        self.alt_es = alt_es
        self.alt_gl = alt_gl
        self.url = url
        self.is_external = is_external
        self.is_social_media = is_social_media
        self.is_contact = is_contact
        self.is_active = is_active

with open('assets/data//links.json', 'r') as archivo:
    # Carga el contenido del archivo JSON en un diccionario
    links = json.load(archivo)

links_references = [
    LinkData(
        item['title_es'],
        item['title_gl'],
        item['description_es'],
        item['description_gl'],
        item['light_icon'],
        item['dark_icon'],
        item['alt_es'],
        item['alt_gl'],
        item['url'],
        item['is_external'],
        item['is_social_media'],
        item['is_contact'],
        item['is_active']
    )
    for item in links
]
