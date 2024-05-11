# DAI Linktree

[![Python](https://img.shields.io/badge/Python-3.11+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)
[![Reflex](https://img.shields.io/badge/Reflex-0.4.9-5646ED?style=for-the-badge&logo=reflex&logoColor=white&labelColor=101010)](https://reflex.dev)
[![Pterodactyl](https://img.shields.io/badge/Pterodactyl-logic&static-blue?style=for-the-badge&logo=pterodactyl&logoColor=white&labelColor=101010)](https://pterodactyl.io/)


## Proyecto Linktree de la Delegación de Alumnos de la Escuela de Ingeniería Industrial (UVigo)
### Modo Claro
![image](https://github.com/Cocotterooo/linktree.dai/assets/103317717/1c5b44ca-59ce-4d76-a9a2-169ef268d8b1)
### Modo Oscuro
![image](https://github.com/Cocotterooo/linktree.dai/assets/103317717/552a8e8a-b689-4cc4-8686-e94f83ab9d7b)

## Añadir nuevos enlaces:
para añadir nuevos enlaces al linktree solo hay que ir a `linktree_dai > assets > data > links.json`, 
una vez ahí añade rellena sus propiedades.
```json
{
    "title": "Nuestra Web",
    "description": "Servicios e información útil para los estudiantes.",
    "light_icon": "/icons/white/social/web.svg",
    "dark_icon": "/icons/blue/social/web.svg",
    "alt": "Logotipo de Aplicación Web",
    "url": "https://dai.uvigo.gal",
    "is_external": true,
    "is_social_media": false,
    "is_active": true
}
```
> **PROPIEDADES:**
> > title -> Título del enlace que aparecerá en la app.
> >
> > description -> Descripción del enlace que aparecerá en la app.
> >
> >
> > alt -> Descripción breve del icono para la accesibilidad.
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

> [!NOTE]
> El orden de aparición de los links se corresponte con el orden dentro del archivo .json

## ¿Cómo hostear el sitio web?
En este caso se ha utilizado una instancia de pterodactil originalmente.

[Para ello puedes encontrár aquí la información](https://github.com/Cocotterooo/docker-pterodactyl-reflex)
