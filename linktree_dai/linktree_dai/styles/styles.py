from enum import Enum

from linktree_dai.styles.fonts import Font, FontWeight

STYLESHEETS = [
    # FUENTE:
    'https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap', # Normal
    'https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap', # Titulos
    'https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap', # Titulos
    '/css/styles.css'
]

BASE_STYLE = {
    'font_size': '16px',
    'font_family': Font.DEFAULT.value,
    'font_weight': FontWeight.LIGHT.value,
    #'color': Color.PRIMARY.value,
    '::selection': {
        'background_color': 'rgba(0, 172, 226, 0.3)',
    }
}

class Size(Enum):
    SMALL = '8px'
    DEFAULT = '16px'
    MEDIUM = '20px'
    MEDIUM_BIG = '24px'
    BIG = '36px'
    LARGE = '50px'
