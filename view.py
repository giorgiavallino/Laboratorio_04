import flet as ft

class View(object):
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

        # define the UI elements and populate the page

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

        # Row 1
        self._dropdown_ricerca = ft.Dropdown(label = "Select a research method",
                                             value = "Choose a research method",
                                             options = [ft.dropdown.Option("Default"),
                                                        ft.dropdown.Option("Lineare"),
                                                        ft.dropdown.Option("Dicotomica")],
                                             on_change = self.__controller.handleResearchMethodSelection())
        self._testo_iniziale = ft.TextField(label = "Insert the text")
        self._bottone_correzione = ft.ElevatedButton("Correggi", on_click = self.__controller.handleSpellChecker)
        row1 = ft.Row([self._dropdown_lingua, self._testo_iniziale, self._bottone_correzione],
                      alignment = ft.MainAxisAlignment.CENTER)

        self._lvOut = ft.ListView()

        self.page.add(self._dropdown_lingua, row1, self._lvOut)

        self.page.update()

    def update(self):
        self.page.update()

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
