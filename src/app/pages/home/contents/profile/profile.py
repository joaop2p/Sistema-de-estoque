from typing import Literal
import flet as ft
from .....widgets.TextField import textFeild
from ......utils.page import Page
from .....models.user import User
from ...interface.model import ContentModel

class Profile(ContentModel):
    def __init__(self) -> None:
        self.user = User()
        self.page = Page().get_page()

    def __str__(self) -> Literal['/profile']:
        return "/profile"

    def getContent(self) -> ft.SafeArea:
        return ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content = ft.Text(
                            value="Profile Details",
                            text_align=ft.TextAlign.CENTER,
                            color=ft.Colors.WHITE,
                            style=ft.TextStyle(
                                weight=ft.FontWeight.BOLD,
                                size=40,
                                font_family="sansation"
                                )
                            ),
                        height=100,
                        alignment=ft.alignment.center,
                        gradient = ft.LinearGradient(
                            colors=[
                                "#00CCF5",
                                "#A868F7",
                                "#4670EB",
                                ],
                            rotation = 0.9
                            ),
                        shadow=ft.BoxShadow(
                            spread_radius=1,
                            blur_radius=5,
                            offset=ft.Offset(
                                x=1,
                                y=4,
                                ),
                            color=ft.Colors.with_opacity(
                                opacity=0.25,
                                color=ft.Colors.BLACK
                                )
                            ),
                        border_radius=ft.BorderRadius(
                            top_left=0,
                            top_right=0,
                            bottom_left=10,
                            bottom_right=10,
                            ),
                        ),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Container(
                                    content = ft.Column(
                                        controls=[
                                            ft.Container(
                                                content=ft.Container(
                                                    content=ft.Image(
                                                        src=self.user.getProfilePhoto(),
                                                        fit=ft.ImageFit.CONTAIN,
                                                        scale=1.5,
                                                        ),
                                                    width=200,
                                                    height=200,
                                                    border_radius=ft.border_radius.all(200),
                                                    ),
                                                alignment=ft.alignment.center,
                                                ),
                                            ft.Container(
                                                content=ft.Text(
                                                    value=f"Bem vindo(a), {self.user.getName()}.",
                                                    text_align=ft.TextAlign.CENTER,
                                                    color=ft.Colors.BLACK,
                                                    size=30,
                                                    style=ft.TextStyle(
                                                        weight=ft.FontWeight.BOLD,
                                                        )
                                                    ),
                                                alignment=ft.alignment.center,
                                                ),
                                            ]
                                        ),
                                    alignment=ft.alignment.center,
                                    ),
                                ft.Divider(),
                                ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            ft.Column(
                                                controls=[
                                                    textFeild(
                                                        label="Nome",
                                                        theme="dark",
                                                        width=None,
                                                        icon=ft.Icons.PERSON,
                                                        value=self.user.getName(),
                                                        read_only=True,
                                                        suffix=ft.Container(
                                                            content=ft.Text(
                                                                value="alterar",
                                                                color="#7685F6",
                                                                weight=ft.FontWeight.BOLD,
                                                                ),
                                                            on_click=lambda  _: print("aa")
                                                            )
                                                        ),
                                                    textFeild(
                                                        label="Email",
                                                        icon=ft.Icons.EMAIL,
                                                        theme="dark",
                                                        width=None,
                                                        value=self.user.getEmail(),
                                                        read_only=True,
                                                        suffix=ft.Container(
                                                            content=ft.Text(
                                                                value="alterar",
                                                                color="#7685F6",
                                                                weight=ft.FontWeight.BOLD,
                                                                ),
                                                            on_click=lambda  _: print("aa")
                                                            )
                                                        ),
                                                    textFeild(
                                                        label="Password",
                                                        icon=ft.Icons.LOCK,
                                                        theme="dark",
                                                        width=None,
                                                        value=self.user.getPassword(),
                                                        read_only=True,
                                                        password = True,
                                                        suffix=ft.Container(
                                                            content=ft.Text(
                                                                value="alterar",
                                                                color="#7685F6",
                                                                weight=ft.FontWeight.BOLD,
                                                                ),
                                                            on_click=lambda  _: print("aa")
                                                            )
                                                        )
                                                    ],
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                )
                                            ]
                                        ),
                                    alignment=ft.alignment.center,
                                    expand_loose=True
                                    )
                                ]
                            ),
                        alignment=ft.alignment.center,
                        padding=ft.padding.all(20),
                        expand=True,
                        )
                    ]
                )
            
            )