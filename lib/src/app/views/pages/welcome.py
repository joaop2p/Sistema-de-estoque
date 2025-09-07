from lib.src.app.styles.theme import ThemeManager
from ...models.interfaces.viewer_page import ViewerPage
from lib.utils.labels import Labels
from lib.utils.label_keys import LabelKey
import flet as ft

class WelcomePage(ViewerPage):
    _theme: ThemeManager

    def __init__(self) -> None:
        self._theme = ThemeManager()

    def get_view(self) -> ft.Container:
        return ft.Container(
            alignment=ft.alignment.center,
            expand=True,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        Labels.t(LabelKey.WELCOME_TITLE),
                        size=30,
                        weight=ft.FontWeight.BOLD,
                        color=self._theme.mode.FONT_COLOR
                    ),
                    ft.Text(
                        Labels.t(LabelKey.WELCOME_INSTRUCTION),
                        size=20,
                        color=self._theme.mode.FONT_COLOR
                    )
                ]
            )
        )
