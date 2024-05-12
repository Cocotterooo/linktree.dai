# DAI Linktree

[![Python](https://img.shields.io/badge/Python-3.11+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)
[![Reflex](https://img.shields.io/badge/Reflex-0.4.9-5646ED?style=for-the-badge&logo=reflex&logoColor=white&labelColor=101010)](https://reflex.dev)
[![Pterodactyl](https://img.shields.io/badge/Pterodactyl-logic&static-blue?style=for-the-badge&logo=pterodactyl&logoColor=white&labelColor=101010)](https://pterodactyl.io/)


## Proyecto Linktree de la Delegación de Alumnos de la Escuela de Ingeniería Industrial (UVigo)
### Modo Claro
![image](https://github.com/Cocotterooo/linktree.dai/assets/103317717/2d0b2315-1d2f-4c45-bb46-9c869866882d)

### Modo Oscuro
![image](https://github.com/Cocotterooo/linktree.dai/assets/103317717/cacb579b-e1c6-42fd-8b83-6529947ef67f)


## Añadir nuevos enlaces:
para añadir nuevos enlaces al linktree solo hay que ir a `linktree_dai > assets > data > links.json`, 
una vez ahí añade rellena sus propiedades.
```json
{
    "title_es": "Nuestra Web",
    "title_gl": "A nosa Web",
    "description_es": "Servicios e información útil para los estudiantes.",
    "description_gl": "Servizos e información útil para os estudantes.",
    "light_icon": "/icons/white/social/web.svg",
    "dark_icon": "/icons/blue/social/web.svg",
    "alt_es": "Logotipo de Aplicación Web",
    "alt_gl": "Logotipo dunha páxina web",
    "url": "https://dai.uvigo.gal",
    "is_external": true,
    "is_social_media": false,
    "is_contact": false,
    "is_active": true
}
```
> **PROPIEDADES:**
> > title es/gl -> Título del enlace que aparecerá en la app. (Ambos Idiomas)
> >
> > description es/gl -> Descripción del enlace que aparecerá en la app. (Ambos Idiomas)
> >
> > alt es/gl -> Descripción breve del icono para la accesibilidad. (Ambos Idiomas)
> >
> > light_icon / dark_icon -> Direcciones a los iconos para el modo oscuro y el modo claro.
> >
> > url -> Enlace :)
> > 
> > is_external -> Se abrirá una nueva pestaña al clickar.
> > 
> > is_social_media -> Aparecerá en la sección Redes Sociales.
> > 
> > is_active -> Se necesita un valor True para que el enlace se renderice en la web.

> [!TIP]
> El orden de aparición de los links se corresponte con el orden dentro del archivo .json

## ¿Cómo hostear el sitio web?
En este caso se ha utilizado una instancia de pterodactil originalmente.
[Para ello puedes encontrár aquí la información](https://github.com/Cocotterooo/docker-pterodactyl-reflex)


> [!NOTE]
> El opción de cambio de idioma entre castellano y gallego está pendiende de mejora para tener ambos idiomas en un archivo separado para su fácil manipulación.
