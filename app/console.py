# TODO: Agrega el código de las clases de la interfaz de usuario aquí. Borra este comentario al terminar.
from rich.prompt import Prompt

class NotebookUI:
    def mostrar_menu(self):
        self.consola.print("\n[bold green]NOTEBOOK[/bold green]")
        self.consola.print("\n 1. Agregar nota")
        self.consola.print("\n2. Listar notas")
        self.consola.print("\n 3. Agregar etiqueta a nota")
        self.consola.print("\n 4. Listar notas importantes")
        self.consola.print("\n 5. Eliminar nota")
        self.consola.print("\n 6. Mostrar notas por etiqueta")
        self.consola.print("\n [bold red]7.Salir [/bold red]")

        opcion = Prompt.ask("\n Seleccione una opcion: ", choices=["1", "2", "3", "4", "5", "6","7"])
        return opcion
