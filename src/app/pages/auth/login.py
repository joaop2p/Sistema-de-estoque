
from ..home.home import Home
from ...widgets.switch import Switch
from ....utils.layout import Layout
from ..interface.model import ViewModel
from ...services.auth import Auth
from ....utils.page import Page
from ...widgets.TextField import textFeild
from ...router.router import Router
import flet as ft

class LoginPage(ViewModel, Auth):
    def __init__(self, debug: bool = False, **kwargs):
        super().__init__()
        self.page = Page().get_page()
        self.router = Router()
        self.debug = debug
        self.route = "/login"
        self.login = ft.Ref[ft.TextField]()
        self.password = ft.Ref[ft.TextField]()
        self.main_content: ft.Container = None
        self.switch = Switch(option_1_value="Sign In",option_2_value="Sign Up", on_click=self._chengeMode)

    @property
    def _inputCheck(self) -> bool:
        self.login.current.error_text = f"Campo {self.login.current.label} é obrigatório." if self.login.current.value.strip() == "" else None
        self.password.current.error_text = f"Campo {self.password.current.label} é obrigatório." if self.password.current.value.strip() == "" else None
        self.page.update()
        return self.password.current.value.strip() != "" and self.login.current.value.strip() != ""

    @property
    def _authCheck(self) -> bool:
        result = self.sign_in(self.login.current.value, self.password.current.value)
        self.login.current.error_text = "O usuário pode está errado." if not result else None
        self.password.current.error_text = "A senha pode está errada." if not result else None
        self.page.update()
        return result

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
                                    on_click=lambda _: self.router.setView(Home()) if self.debug or self._inputCheck and self._authCheck else None,
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
                            content = ft.Text(
                                spans=[
                                    ft.TextSpan(
                                            text="Esqueci a senha",
                                            on_click=lambda _: (print("Em construção"), print(self.page.width))
                                        )
                                    ],
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
            print(self._signInView())
            self.main_content.content = self._signInView()
        else:
            print(self._signUpView())
            self.main_content.content = self._signUpView()
        self.main_content.update()
        

    def get_view(self) -> ft:
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