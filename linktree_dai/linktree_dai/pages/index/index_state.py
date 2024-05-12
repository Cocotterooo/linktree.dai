import reflex as rx

class IndexState(rx.State):
    light_mode_save: str = rx.LocalStorage(sync=True)  # Local Storage solo funciona con str
    language_save: str = rx.LocalStorage(sync=True)  # Local Storage solo funciona con str

    def toggle_language(self):
        # Cambiar el idioma y guardar el nuevo valor en language_save
        if self.language_save.lower() in ['true', '1']:
            self.language_save = 'false'
        else:
            self.language_save = 'true'

    @rx.var
    def lang_mode(self) -> bool:
        # Convertir language_save a bool cada vez que se acceda a lang_mode
        return self.language_save.lower() in ['true', '1']

    def toggle_theme(self):
        if self.light_mode_save.lower() in ['true', '1']:
            self.light_mode_save = 'false'
        else:
            self.light_mode_save = 'true'

    @rx.var
    def light_mode(self) -> bool:
        return self.light_mode_save.lower() in ['true', '1']

    @rx.var
    def primary_color(self) -> str:
        return '#003749' if self.light_mode else '#E5F7FF'

    @rx.var
    def accent_color(self) -> str:
        return '#00ACE2'

    @rx.var
    def secondary_color(self) -> str:
        return '#E5F7FF' if self.light_mode else '#003749'
    
    def on_load(self):
        pass