# Importare tutti i moduli che verranno utlizzati in seguito: flet, controller e view
import flet as ft
from controller import SpellChecker
from view import View

# Definizione del main
def main(page: ft.Page):
    # Istanziare la view e il controller
    view = View(page)
    controller = SpellChecker(view)
    view.setController(controller)
    # Aggiungere l'interfaccia grafica
    view.add_content()

# Inserire il seguente codice, necessario per la visualizzazione grafica
ft.app(target = main)