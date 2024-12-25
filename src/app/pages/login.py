
from ..widgets.switch import Switch

from ..widgets.text_link import text_link
from ...utils.layout import Layout
from .model.model import ViewModel
from ..services.auth import Auth
from ...utils.page import Page
from ..widgets.warning_bar import error_warning
from ..widgets.TextField import textFeild
import flet as ft

class LoginPage(ViewModel, Auth):
    def __init__(self):
        super().__init__()
        self.page = Page().get_page()
        self.route = "/home"
        self.login = ft.Ref[ft.TextField]()
        self.password = ft.Ref[ft.TextField]()
        self.main_content: ft.Container = None
        self.switch = Switch(option_1_value="Sign In",option_2_value="Sign Up", on_click=self._chengeMode)

    def _inputCheck(self):
        self.login.current.error_text = f"Campo {self.login.current.label} é obrigatório." if self.login.current.value.strip() == "" else None
        self.password.current.error_text = f"Campo {self.password.current.label} é obrigatório." if self.password.current.value.strip() == "" else None
        self.page.update()
        return self.password.current.value.strip() != "" and self.login.current.value.strip() != ""

    def _signInView(self) -> ft.Container:
        return ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Text(
                                value="Sign In",
                                text_align=ft.TextAlign.CENTER,
                                style=ft.TextStyle(
                                    color=ft.Colors.WHITE,
                                    size=30,
                                    weight=ft.FontWeight.BOLD,
                                    )
                                ),
                            alignment=ft.alignment.center
                            ),
                        ft.Container(
                            content=textFeild(
                                label="Login",
                                ref=self.login,          
                                max_length=6,
                                icon=ft.Icons.PERSON
                                ),
                            alignment=ft.alignment.center
                            ),
                        ft.Container(
                            content=textFeild(
                                label="Senha",
                                ref=self.password,          
                                max_length=8,
                                password=True,
                                can_reveal_password=True,
                                icon=ft.Icons.LOCK
                                ),
                            alignment=ft.alignment.center
                            ),
                        ft.Container(
                            height=Layout.getHeight(0.01)
                            ),
                        ft.Container(
                            content=ft.Container(
                                content=ft.ElevatedButton(
                                    content=ft.Text(
                                        value="Entrar"
                                        ),
                                    bgcolor="#6CA2F2",
                                    style=ft.ButtonStyle(
                                        padding=20,
                                        color=ft.Colors.WHITE
                                        ),
                                    on_click=lambda _: (print("aproved") if self._inputCheck() else print("denied")),
                                    width=Layout.getWidth(0.05)
                                    ),
                                ),
                            alignment=ft.alignment.center,
                            adaptive=True
                            ),
                        ft.Container(
                            height=Layout.getHeight(0.01)
                            ),
                        ft.Container(
                            content= text_link(
                                value_text="Esqueci a senha",
                                action= lambda _: print("Senha")
                                ),
                            alignment= ft.alignment.center,
                            )
                        ],
                    alignment=ft.MainAxisAlignment.CENTER
                    ),
                height=Layout.getHeight(0.51),
                width=Layout.getWidth(0.27),
                bgcolor="#D9D9D9",
                border_radius=ft.border_radius.all(10),
                gradient = ft.LinearGradient(
                    colors=[
                        "#00CCF5",
                        "#A868F7",
                        ],
                    rotation = 0.9
                    )
                )

    def _signUpView(self) -> ft.Container:
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Text(
                            value="Sign Up",
                            text_align=ft.TextAlign.CENTER,
                            style=ft.TextStyle(
                                color=ft.Colors.WHITE,
                                size=30,
                                weight=ft.FontWeight.BOLD,
                                )
                            ),
                        alignment=ft.alignment.center
                        ),
                    ft.Container(
                        content=textFeild(
                            label="Email",
                            hint_text="email@exemple.com",
                            max_length=None,
                            icon=ft.Icons.EMAIL
                            ),
                        alignment=ft.alignment.center
                        ),
                    ft.Container(
                        content=textFeild(
                            label="Login",
                            max_length=None,
                            icon=ft.Icons.PERSON
                            ),
                        alignment=ft.alignment.center
                        ),
                    ft.Container(
                        content=textFeild(
                            label="Senha", 
                            max_length=8,
                            password=True,
                            can_reveal_password=True,
                            icon=ft.Icons.LOCK
                            ),
                        alignment=ft.alignment.center
                        ),
                    ft.Container(
                        content=textFeild(
                            label="Confirmar Senha", 
                            max_length=8,
                            password=True,
                            can_reveal_password=True,
                            icon=ft.Icons.LOCK
                            ),
                        alignment=ft.alignment.center
                        ),
                    ft.Container(
                        height=Layout.getHeight(0.01)
                        ),
                    ft.Container(
                        content=ft.Container(
                            content=ft.ElevatedButton(
                                content=ft.Text(
                                    value="Cadastrar"
                                    ),
                                bgcolor="#6CA2F2",
                                style=ft.ButtonStyle(
                                    padding=20,
                                    color=ft.Colors.WHITE
                                    ),
                                ),
                            ),
                        alignment=ft.alignment.center,
                        adaptive=True
                        ),
                    ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            height=Layout.getHeight(0.51),
            width=Layout.getWidth(0.27),
            bgcolor="#D9D9D9",
            border_radius=ft.border_radius.all(10),
            gradient = ft.LinearGradient(
                colors=[
                    "#00CCF5",
                    "#A868F7",
                    ],
                rotation = -8.5
                )
            )

    def _chengeMode(self):
        if self.switch.getCurrentOption == "Sign In":
            self.main_content.content = self._signInView()
        else:
            self.main_content.content = self._signUpView()
        self.main_content.update()
        

    def get_view(self) -> ft:
        # self.main_content = ft.Container(content=self._signInView(), animate_opacity=ft.AnimatedSwitcher(, ft.AnimationCurve.EASE))
        self.main_content = ft.AnimatedSwitcher(
            content=self._signInView(), duration= 1000, 
            transition=ft.AnimatedSwitcherTransition.FADE
            )
        return ft.View(
            route=self.route,
            controls=[
                ft.ResponsiveRow(
                    controls=[
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Container(
                                        content = self.switch.get(),
                                        alignment=ft.alignment.center,
                                        ),
                                    ft.Container(
                                        content = self.main_content,
                                        alignment=ft.alignment.center,
                                        ),
                                    ],
                                alignment=ft.MainAxisAlignment.CENTER
                                ),
                            width=self.page.window.width,
                            height=self.page.window.height,
                            bgcolor="#8694F2",
                            alignment=ft.alignment.center,
                            gradient=ft.LinearGradient(
                                colors=[
                                    "#6CA2F2", "#8694F2"
                                    ]
                                )
                            ),
                        ],
                    alignment=ft.MainAxisAlignment.CENTER
                    ),
                ],
            padding=0
            )