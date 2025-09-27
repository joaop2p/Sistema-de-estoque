
from typing import Callable
from lib.src.app.models.interfaces.viewer_page import ViewerPage
from lib.src.app.styles.image import ImagesAssets
from lib.src.app.styles.theme import ThemeManager
from lib.src.app.views.pages.clients_view import ClientView
from lib.src.app.views.pages.home_view import HomeView
from lib.src.app.views.pages.products_view import ProductView
from lib.src.app.views.pages.sales_view import SalesView
from lib.src.app.views.pages.welcome_view import WelcomeView
from lib.src.app.views.widgets.side_bar import SideBar
from lib.src.config.app_config import AppConfig
from ..models.interfaces.app_page import AppPage
from flet import Page, View, Container, Text
import flet as ft
from lib.utils.labels.labels import Labels
from lib.utils.labels.label_keys import LabelKey

class MainView(AppPage):
    _page: Page
    _name: str = '/main_view'
    _side_bar: SideBar
    _main_content_controller: ft.Ref[ft.Container]

    def __init__(self) -> None:
        self._theme = ThemeManager()
        self._side_bar = SideBar(self._theme)
        self._main_content_controller = ft.Ref[ft.Container]()
        self._config = AppConfig.get_instance()

    def set_page(self, page: Page):
        self._page = page

    def teste_2(self):
        return ft.Text("Teste 2")
    
    def _content_selector(self, index: int = 0):
        keys = list(self.options.keys())
        if self._config.first_init:
            self._config.update_first_init()
        if keys[index] == 'logout':
            print('Logout clicked')
            self._page.go('/login')
            return
        view: ViewerPage = self.options[keys[index]]['view']
        self._main_content_controller.current.content = view.get_view()
        self._main_content_controller.current.update()

    def get_page(self) -> View:
        self.options: dict[str, dict] = {
            'home': {
                'icon': ft.Icons.HOME,
                'selected_icon': ft.Icons.HOME_FILLED,
                'label': Labels.t(LabelKey.MENU_HOME),
                'view': HomeView()
            },
            'products': {
                'icon': ft.Icons.INVENTORY_2,
                'selected_icon': ft.Icons.INVENTORY_2,
                'label': Labels.t(LabelKey.MENU_PRODUCTS),
                'view': ProductView()
            },
            'clients': {
                'icon': ft.Icons.GROUP,
                'selected_icon': ft.Icons.GROUP,
                'label': Labels.t(LabelKey.MENU_CLIENTS),
                'view': ClientView(self._page)
            },
            'sales': {
                'icon': ft.Icons.POINT_OF_SALE,
                'selected_icon': ft.Icons.POINT_OF_SALE,
                'label': Labels.t(LabelKey.MENU_SALES),
                'view': SalesView()
            },
            'profile': {
                'icon': ft.Icons.PERSON,
                'selected_icon': ft.Icons.PERSON,
                'label': Labels.t(LabelKey.MENU_PROFILE),
                'view': HomeView()
            },
            'settings': {
                'icon': ft.Icons.SETTINGS,
                'selected_icon': ft.Icons.SETTINGS,
                'label': Labels.t(LabelKey.MENU_SETTINGS),
                'view': HomeView()
            },
            'logout': {
                'icon': ft.Icons.LOGOUT,
                'selected_icon': ft.Icons.LOGOUT,
                'label': Labels.t(LabelKey.MENU_LOGOUT),
                'view': HomeView()
            },
        }
        section = 'sales'
        first_view = self.options[section].get('view', self._config.first_init).get_view()
        # self._content_selector()
        return View(
            self._name,
            vertical_alignment = ft.MainAxisAlignment.CENTER,
            padding=0,
            controls=[
                # Apenas para ter conteúdo na página
                Container(
                    expand=True,
                    alignment=ft.alignment.center,
                    bgcolor=self._theme.mode.BODY_COLOR,
                    content=ft.Row(
                        spacing=5,
                        controls=[
                            self._side_bar.menu(self.options, self._content_selector, list(self.options.keys()).index(section)),
                            # ft.VerticalDivider(width=1),
                            ft.Container(
                                expand=True,
                                ref=self._main_content_controller,
                                content=first_view,
                            )
                        ]
                    )
                )
            ]
        )
    