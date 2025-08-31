from typing import Any
import flet as ft

from lib.src.app.views.widgets.text_field import text_Feild
from lib.src.app.views.widgets.toggle import Toggle
from ..models.interfaces.app_page import AppPage
from ....utils.label_keys import LabelKey
from ....utils.labels import Labels

class Login(AppPage):
    _name = '/login'
    _labels = Labels
    _keys = LabelKey
    _refs: dict[str, dict[str, dict[str, ft.Ref]]]
    _toggle: Toggle

    def __init__(self) -> None:
        self._refs = {
            'fields':{
                'signIn':{
                    'login': ft.Ref[ft.TextField](),
                    'password': ft.Ref[ft.TextField]()
                },
                'signUp':{
                    'login': ft.Ref[ft.TextField](),
                    'email': ft.Ref[ft.TextField](),
                    'password': ft.Ref[ft.TextField](),
                    'confirm_password': ft.Ref[ft.TextField](),
                }
            },
            'objects':{
                'containers': {
                    'main_content_area': ft.Ref[ft.Container](),
                    'field_container': ft.Ref[ft.Container]()
                }
            }
        }
        

    def set_page(self, page: ft.Page) -> None:
        self._page = page

    @property
    def _inputCheck(self) -> bool:
        login = self._refs['signIn']['fields']['login']
        password = self._refs['signIn']['fields']['password']
        login.current.error_text = f"Campo {login.current.label} é obrigatório." if not login.current.value else None
        password.current.error_text = f"Campo {password.current.label} é obrigatório." if not password.current.value else None
        self._page.update()
        return bool(password.current.value) and bool(login.current.value)

    def _area_base(self,title: str, control: ft.Control):
        return ft.Container(
            alignment=ft.alignment.center,
            ref = self._refs['objects']['containers']['field_container'],
            width=550,
            height=500,
            border_radius=5,
            gradient=ft.LinearGradient(
                colors=[
                    "#00CCF5",
                    "#A868F7",
                    ],
                rotation = -8.5
                ),
            shadow=ft.BoxShadow(
                spread_radius=5,
                blur_radius=15,
                color=ft.Colors.with_opacity(0.1,ft.Colors.BLACK),
                offset=ft.Offset(0,1)
            ),
            content= ft.AnimatedSwitcher(
                duration=100,
                transition=ft.AnimatedSwitcherTransition.FADE,
                content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        alignment=ft.alignment.center,
                        padding=10,
                        content=ft.Text(
                            title,
                            text_align=ft.TextAlign.CENTER,
                            style=ft.TextStyle(
                                weight=ft.FontWeight.BOLD,
                                overflow = ft.TextOverflow.FADE,
                                size=24,
                            )
                        ),
                    ),
                    control
                ]
            )
        )
    )
    @property
    def _sing_up(self) -> ft.Container:
        temp_refs = self._refs['fields']['signUp']
        return ft.Container(
                alignment=ft.alignment.center,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            alignment=ft.alignment.center,
                            content=text_Feild(
                                label=self._labels.t(self._keys.LOGIN_FIELD),
                                ref=temp_refs['login'],          
                                max_length=6,
                                icon=ft.Icons.PERSON,
                            )
                        ),
                        ft.Container(
                            alignment=ft.alignment.center,
                            content=text_Feild(
                                label=self._labels.t(self._keys.MAIL_FIELD),
                                ref=temp_refs['email'],          
                                icon=ft.Icons.MAIL,
                            )
                        ),
                        ft.Container(
                            alignment=ft.alignment.center,
                            content=text_Feild(
                                label=self._labels.t(self._keys.PASSWORD_FIELD),
                                ref=temp_refs['password'],          
                                icon=ft.Icons.LOCK_OUTLINE,
                                password=True,
                                can_reveal_password = True
                            )
                        ),
                        ft.Container(
                            alignment=ft.alignment.center,
                            content=text_Feild(
                                label=self._labels.t(self._keys.COFIRM_PASSWORD),
                                ref=temp_refs['confirm_password'],          
                                icon=ft.Icons.LOCK_OUTLINE,
                                password=True,
                                can_reveal_password = True
                            )
                        ),
                        ft.Container(
                            height=10
                        ),
                        ft.Container(
                            content=ft.Container(
                                content=ft.ElevatedButton(
                                    bgcolor="#6CA2F2",
                                    on_click=lambda _: print(self._inputCheck),
                                    style=ft.ButtonStyle(
                                        padding=20,
                                        color=ft.Colors.WHITE
                                        ),
                                    content=ft.Text(
                                        self._labels.t(self._keys.SIGN_UP)
                                        ),
                                    ),
                                ),
                            alignment=ft.alignment.center,
                            adaptive=True
                        )
                    ]
                )
            )

    @property
    def _sing_in(self) -> ft.Container:
        temp_refs = self._refs['fields']['signIn']
        return ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=text_Feild(
                                    label=self._labels.t(self._keys.LOGIN_FIELD),
                                    ref=temp_refs['login'],          
                                    max_length=6,
                                    icon=ft.Icons.PERSON,
                                )
                            ),
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=text_Feild(
                                    label=self._labels.t(self._keys.PASSWORD_FIELD),
                                    ref=temp_refs['password'],          
                                    icon=ft.Icons.LOCK_OUTLINE,
                                    password=True,
                                    can_reveal_password = True
                                )
                            ),
                            ft.Container(
                                height=10
                            ),
                            ft.Container(
                                content=ft.Container(
                                    content=ft.ElevatedButton(
                                        bgcolor="#6CA2F2",
                                        on_click=lambda _: print(self._inputCheck),
                                        style=ft.ButtonStyle(
                                            padding=20,
                                            color=ft.Colors.WHITE
                                            ),
                                        content=ft.Text(
                                            self._labels.t(self._keys.LOGIN_MESSAGE)
                                            ),
                                        ),
                                    ),
                                alignment=ft.alignment.center,
                                adaptive=True
                            )
                        ]
                    )
                )
    def _chengeMode(self):
        content_area = self._refs['objects']['containers']['main_content_area']
        field_container = self._refs['objects']['containers']['field_container']
        if self._toggle.current_option == Labels.t(LabelKey.SIGN_IN):
            content_area.current.content = self._area_base(title= self._labels.t(self._keys.WELCOME),control=self._sing_in)
            field_container.current.gradient=ft.LinearGradient(colors=["#00CCF5", "#A868F7"],rotation = -8.5)
        else:
            content_area.current.content = self._area_base(title= self._labels.t(self._keys.WELCOME),control=self._sing_up)
            field_container.current.gradient=ft.LinearGradient(colors=["#A868F7", "#00CCF5"],rotation = -8.5)
        self._page.update()

    def get_page(self) -> ft.View:
        self._toggle = Toggle(option_1_value=Labels.t(LabelKey.SIGN_IN),option_2_value=Labels.t(LabelKey.SIGN_UP), on_click=self._chengeMode, page= self._page)
        return ft.View(
            self._name,
            padding=0,
            vertical_alignment = ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    alignment=ft.alignment.center,
                    expand=True,
                    gradient=ft.LinearGradient(
                        colors=["#6CA2F2", "#8694F2"]
                    ),
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=self._toggle.get()
                            ),
                            ft.Container(
                                ref=self._refs['objects']['containers']['main_content_area'],
                                alignment=ft.alignment.center,
                                content=ft.AnimatedSwitcher(
                                    duration=1000,
                                    transition=ft.AnimatedSwitcherTransition.FADE,
                                    content=self._area_base(
                                    title= self._labels.t(self._keys.WELCOME),
                                    control=self._sing_in
                                )
                            )
                        ),
                    ]
                )
            )
        ]
    )