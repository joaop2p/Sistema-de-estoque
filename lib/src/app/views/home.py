
from typing import Callable
from lib.src.app.styles.image import ImagesAssets
from lib.src.app.styles.theme import ThemeManager
from lib.src.app.views.widgets.side_bar import SideBar
from ..models.interfaces.app_page import AppPage
from flet import Page, View, Container, Text
import flet as ft
from lib.utils.labels import Labels
from lib.utils.label_keys import LabelKey

class Home(AppPage):
    _page: Page
    _name: str = '/home'
    _side_bar: SideBar

    def __init__(self) -> None:
        self._theme = ThemeManager()
        self._side_bar = SideBar(self._theme)

    def set_page(self, page: Page):
        self._page = page
        

    def get_page(self) -> View:
        options = {
            'home': {
                'icon': ft.Icons.HOME,
                'selected_icon': ft.Icons.HOME_FILLED,
                'label': Labels.t(LabelKey.MENU_HOME),
                'on_click': lambda e: self._page.go('/home')
            },
            'products': {
                'icon': ft.Icons.INVENTORY_2,
                'selected_icon': ft.Icons.INVENTORY_2,
                'label': Labels.t(LabelKey.MENU_PRODUCTS),
                'on_click': lambda e: self._page.go('/products')
            },
            'clients': {
                'icon': ft.Icons.GROUP,
                'selected_icon': ft.Icons.GROUP,
                'label': Labels.t(LabelKey.MENU_CLIENTS),
                'on_click': lambda e: self._page.go('/clients')
            },
            'sales': {
                'icon': ft.Icons.POINT_OF_SALE,
                'selected_icon': ft.Icons.POINT_OF_SALE,
                'label': Labels.t(LabelKey.MENU_SALES),
                'on_click': lambda e: self._page.go('/sales')
            },
            'profile': {
                'icon': ft.Icons.PERSON,
                'selected_icon': ft.Icons.PERSON,
                'label': Labels.t(LabelKey.MENU_PROFILE),
                'on_click': lambda e: self._page.go('/profile')
            },
            'settings': {
                'icon': ft.Icons.SETTINGS,
                'selected_icon': ft.Icons.SETTINGS,
                'label': Labels.t(LabelKey.MENU_SETTINGS),
                'on_click': lambda e: self._page.go('/settings')
            },
                'logout': {
                'icon': ft.Icons.LOGOUT,
                'selected_icon': ft.Icons.LOGOUT,
                'label': Labels.t(LabelKey.MENU_LOGOUT),
                'on_click': lambda e: self._page.go('/login')
            },
        }
        return View(
            self._name,
            padding=0,
            controls=[
                # Apenas para ter conteúdo na página
                Container(
                    expand=True,
                    bgcolor=self._theme.mode.BODY_COLOR,
                    content=ft.Row(
                        spacing=5,
                        controls=[
                            self._side_bar.menu(self._page.height, options),
                            # ft.VerticalDivider(width=1),
                            ft.Container(
                                expand=True, 
                                # content=
                            )
                        ]
                    )
                )
            ]
        )
    