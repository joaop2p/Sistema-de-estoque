from lib.src.models.interfaces.app_page import AppPage
from flet import Page, View, Container, Text

class Home(AppPage):
    _page: Page
    _name: str = '/home'

    def set_page(self, page: Page):
        self._page = page

    def get_page(self) -> View:
        return View(
            self._name,
            controls=[
                # Apenas para ter conteúdo na página
                Container(
                    content=Text('Oi')
                )
            ]
        )
    