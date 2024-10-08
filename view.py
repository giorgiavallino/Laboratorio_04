# Importare i moduli che serviranno in seguito
import flet as ft

# Definire una classe View
class View(object):

    # Definire il metodo __init__ in cui si fa riferimento alla pagina dell'interfaccia grafica che dovrà essere
    # aggiornata per aggiungere gli elementi grafici necessari e richiesti dall'esercizio
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None
        self._dropdown_lingua = None
        self._dropdown_ricerca = None
        self._testo_iniziale = None
        self._bottone_correzione = None
        self._lvOut = None

    # Definire un metodo che gestisca e aggiunga elementi all'interfaccia grafica
    def add_content(self): # Function that creates and adds the visual elements to the page. It also updates
    # the page accordingly

        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Row 1
        self._dropdown_lingua = ft.Dropdown(label = "Select language",
                                      value = "Choose a language",
                                      options = [ft.dropdown.Option("English"),
                                                 ft.dropdown.Option("Italian"),
                                                 ft.dropdown.Option("Spanish")],
                                      autofocus = True,
                                      on_change = self.__controller.handleLangSelection())

        # Row 2
        self._dropdown_ricerca = ft.Dropdown(label = "Select a research method",
                                             value = "Choose a research method",
                                             options = [ft.dropdown.Option("Default"),
                                                        ft.dropdown.Option("Lineare"),
                                                        ft.dropdown.Option("Dicotomica")],
                                             on_change = self.__controller.handleResearchMethodSelection())
        self._testo_iniziale = ft.TextField(label = "Insert the sentence")
        self._bottone_correzione = ft.ElevatedButton("Correction",
                                                     on_click = self.__controller.handleSpellChecker)
        row1 = ft.Row([self._dropdown_lingua, self._testo_iniziale, self._bottone_correzione],
                      alignment = ft.MainAxisAlignment.CENTER)

        # Row 3
        self._lvOut = ft.ListView()

        # Aggiunta degli elementi alla pagina
        self.page.add(self._dropdown_lingua, row1, self._lvOut)

        self.page.update()

    # Definire il metodo update per evitare di scrivere ogi volta page.update
    def update(self):
        self.page.update()

    # Definire il metodo setController per creare una correlazione tra la view e il controller nel main
    def setController(self, controller):
        self.__controller = controller

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
