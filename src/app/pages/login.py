from ...utils.layout import Layout
from .model.model import ViewModel
from ...utils.page import Page
import flet as ft

class LoginPage(ViewModel):
    def __init__(self):
        self.page = Page().get_page()
        self.route = "/home"
        self.login = ft.Ref[ft.TextField]()
        self.password = ft.Ref[ft.TextField]()

    def get_view(self) -> ft:
        return ft.View(
            route=self.route,
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Container(
                                            content=ft.Text(
                                                value="Entrar",
                                                text_align=ft.TextAlign.CENTER,
                                                style=ft.TextStyle(
                                                    color=ft.Colors.BLACK,
                                                    size=30,
                                                    weight=ft.FontWeight.BOLD,
                                                    )
                                                ),
                                            alignment=ft.alignment.center
                                            ),
                                        ft.Container(
                                            content=ft.TextField(
                                                label="Login",
                                                ref=self.login,
                                                label_style=ft.TextStyle(
                                                    color=ft.Colors.BLACK
                                                    ),
                                                text_style = ft.TextStyle(
                                                    color=ft.Colors.BLACK
                                                    ),
                                                width=Layout.getWidth(0.19)
                                                ),
                                            alignment=ft.alignment.center
                                            ),
                                        ft.Container(
                                            content=ft.TextField(
                                                label="Senha",
                                                ref=self.password,
                                                label_style=ft.TextStyle(
                                                    color=ft.Colors.BLACK
                                                    ),
                                                text_style = ft.TextStyle(
                                                    color=ft.Colors.BLACK
                                                    ),
                                                width=Layout.getWidth(0.19),
                                                password=True
                                                ),
                                            alignment=ft.alignment.center
                                            ),
                                        ft.Container(
                                            content=ft.Container(
                                                content=ft.ElevatedButton(
                                                    content=ft.Text(
                                                        value="Enviar"
                                                        ),
                                                    bgcolor=ft.Colors.GREEN,
                                                    style=ft.ButtonStyle(
                                                        padding=20,
                                                        color=ft.Colors.WHITE
                                                        ),
                                                    on_click=lambda _: print(self.password.current.value, self.login.current.value)
                                                    ),
                                                width=Layout.getWidth(0.19),
                                                alignment=ft.alignment.center_right
                                                ),
                                            alignment=ft.alignment.center,
                                            adaptive=True
                                            )
                                        ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                    ),
                                height=Layout.getHeight(0.51),
                                width=Layout.getWidth(0.27),
                                bgcolor="#D9D9D9",
                                border_radius=ft.border_radius.all(10)
                                )
                            ],
                        alignment=ft.MainAxisAlignment.CENTER
                        ),
                    width=self.page.window.width,
                    height=self.page.window.height,
                    bgcolor=ft.Colors.GREY_900,
                    alignment=ft.alignment.center
                    )
                ],
            padding=0
            )