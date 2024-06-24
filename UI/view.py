import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("SIMULAZIONE D'ESAME 30-31/05/203", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        self.txt_prodotti = ft.TextField(
            label="N. Prodotti in Comune",
            width=200,
        )
        self.dd_nazione = ft.Dropdown(
            label="Nazione",
        )
        self.dd_anno = ft.Dropdown(
            label="Anno",
        )
        self.dd_rivenditore = ft.Dropdown(
            label="Rivenditore",
        )
        self._controller.fillDD()

        # button for the "hello" reply
        self.btn_grafo = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handle_grafo)
        self.btn_analizza = ft.ElevatedButton(text="Analizza Componente", on_click=self._controller.handle_analizza)
        row1 = ft.Row([self.txt_prodotti,self.dd_rivenditore, self.btn_analizza],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        row2 = ft.Row([self.dd_nazione, self.dd_anno, self.btn_grafo],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
