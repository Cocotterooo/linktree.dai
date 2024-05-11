import json

class LinkData:
    def __init__(
            self,
            title: str,
            description: str,
            light_icon: str,
            dark_icon: str,
            alt: str,
            url: str,
            is_external: bool
        ):
        self.title = title
        self.description = description
        self.light_icon = light_icon
        self.dark_icon = dark_icon
        self.alt = alt
        self.url = url
        self.is_external = is_external

with open('assets/data//links.json', 'r') as archivo:
    # Carga el contenido del archivo JSON en un diccionario
    links = json.load(archivo)

links_references = [
    LinkData(
        item['title'],
        item['description'],
        item['light_icon'],
        item['dark_icon'],
        item['alt'],
        item['url'],
        item['is_external']
    )
    for item in links
]
