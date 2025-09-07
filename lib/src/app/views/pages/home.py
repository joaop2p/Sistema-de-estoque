from lib.src.app.models.interfaces.viewer_page import ViewerPage
from lib.src.app.styles.theme import ThemeManager
import flet as ft

from lib.utils.label_keys import LabelKey
from lib.utils.labels import Labels

class Home(ViewerPage):
    _theme: ThemeManager

    def __init__(self) -> None:
        super().__init__()
        self._theme = ThemeManager()
        self._page = None

    def get_view(self) -> ft.Container:
        return ft.Container(
            alignment=ft.alignment.center,
            expand=True,
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(
                                Labels.t(LabelKey.WELCOME),
                                size=30,
                                weight=ft.FontWeight.BOLD,
                                color=self._theme.mode.FONT_COLOR
                            )
                        ]
                    )
                ]
            )
        )