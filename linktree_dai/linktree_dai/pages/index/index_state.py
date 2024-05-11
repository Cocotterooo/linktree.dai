import reflex as rx

class IndexState(rx.State):
    light_mode: bool = True
    first_load: bool = True

    def on_load(self):  # Método para ser llamado en el evento on_load
        self.first_load = False  # Actualizar el indicador de primera carga

    def toggle_theme(self):
        if not self.first_load:
            self.light_mode = not self.light_mode

    @rx.var
    def primary_color(self) -> str:
        return '#003749' if self.light_mode else '#E5F7FF'

    @rx.var
    def accent_color(self) -> str:
        return '#00ACE2'  # Este color permanece igual en ambos modos por simplicidad

    @rx.var
    def secondary_color(self) -> str:
        return '#E5F7FF' if self.light_mode else '#003749'
