from typing import Any
import flet as ft

from lib.src.app.styles.theme import ThemeManager
from lib.src.app.views.widgets.buttom import ButtomLogin
from lib.src.app.views.widgets.text_field import InputField
from lib.src.app.views.widgets.toggle import Toggle
from ..models.interfaces.app_page import AppPage
from ....utils.labels.label_keys import LabelKey
from ....utils.labels.labels import Labels

class Login(AppPage):
    _name = '/login'
    _labels = Labels
    _keys = LabelKey
    _refs: dict[str, dict[str, dict[str, ft.Ref]]]
    _toggle: Toggle
    _theme: ThemeManager

    def __init__(self) -> None:
        self._theme = ThemeManager()
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

    def _inputCheck(self, args:dict[str, dict[str, ft.Ref]]) -> bool:
        aproved = True
        for key, ref in args['fields'].items():
            if not ref.current.value:
                ref.current.error_text = self._labels.t(self._keys.ERROR_TEXT).format(field_name=ref.current.label)
                aproved = False
            else:
                if key == 'confirm_password' and args['fields']['password'].current.value != ref.current.value:
                    ref.current.error_text = self._labels.t(self._keys.ERROR_TEXT_PASSWORD_NOT_MATCH)
                    aproved = False
                else:
                    ref.current.error_text = None
        self._page.update()
        return aproved

    def _area_base(self,title: str, control: ft.Control) -> ft.Container:
        return ft.Container(
            alignment=ft.alignment.center,
            ref = self._refs['objects']['containers']['field_container'],
            width=550,
            height=500,
            border_radius=5,
            gradient=ft.LinearGradient(
                colors=self._theme.mode.PRIMARY_GRADIENT,
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
        buttom = ButtomLogin(text=self._labels.t(self._keys.SIGN_UP), theme = self._theme.mode.name, on_click=self._inputCheck, fields=self._refs['fields']['signUp'])
        return ft.Container(
                alignment=ft.alignment.center,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            alignment=ft.alignment.center,
                            content=InputField.default(
                                theme=self._theme.mode.OBJECT_COLOR,
                                label=self._labels.t(self._keys.LOGIN_FIELD),
                                ref=temp_refs['login'],          
                                max_length=6,
                                icon=ft.Icons.PERSON,
                            )
                        ),
                        ft.Container(
                            alignment=ft.alignment.center,
                            content=InputField.default(
                                theme=self._theme.mode.OBJECT_COLOR,
                                label=self._labels.t(self._keys.MAIL_FIELD),
                                ref=temp_refs['email'],          
                                icon=ft.Icons.MAIL,
                            )
                        ),
                        ft.Container(
                            alignment=ft.alignment.center,
                            content=InputField.default(
                                theme=self._theme.mode.OBJECT_COLOR,
                                label=self._labels.t(self._keys.PASSWORD_FIELD),
                                ref=temp_refs['password'],          
                                icon=ft.Icons.LOCK_OUTLINE,
                                password=True,
                                can_reveal_password = True
                            )
                        ),
                        ft.Container(
                            alignment=ft.alignment.center,
                            content=InputField.default(
                                theme=self._theme.mode.OBJECT_COLOR,
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
                                content=buttom.get
                            ),
                            alignment=ft.alignment.center,
                            adaptive=True
                        )
                    ]
                )
            )

    @property
    def _sing_in(self) -> ft.Container:
        #on_click=self._inputCheck,
        temp_refs = self._refs['fields']['signIn']
        buttom = ButtomLogin(text=self._labels.t(self._keys.SIGN_IN),on_click=lambda _: self._page.go('/main_view'), theme = self._theme.mode.name,  fields=self._refs['fields']['signIn'],)
        return ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=InputField.default(
                                    theme=self._theme.mode.OBJECT_COLOR,
                                    label=self._labels.t(self._keys.LOGIN_FIELD),
                                    ref=temp_refs['login'],          
                                    max_length=6,
                                    icon=ft.Icons.PERSON,
                                )
                            ),
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=InputField.default(
                                    theme=self._theme.mode.OBJECT_COLOR,
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
                                content=buttom.get,
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
            content_area.current.content.content = self._area_base(title= self._labels.t(self._keys.WELCOME),control=self._sing_in)
            self._theme.mode.PRIMARY_GRADIENT.reverse()
            field_container.current.gradient=ft.LinearGradient(colors=self._theme.mode.PRIMARY_GRADIENT,rotation = -8.5)
        else:
            content_area.current.content.content = self._area_base(title= self._labels.t(self._keys.WELCOME),control=self._sing_up)
            self._theme.mode.PRIMARY_GRADIENT.reverse()
            field_container.current.gradient=ft.LinearGradient(colors=self._theme.mode.PRIMARY_GRADIENT,rotation = -8.5)
        self._page.update()

    def get_page(self) -> ft.View:
        self._toggle = Toggle(option_1_value=Labels.t(LabelKey.SIGN_IN),option_2_value=Labels.t(LabelKey.SIGN_UP), on_click=self._chengeMode, page= self._page, theme=self._theme.mode.name)
        print(self._page.height)
        return ft.View(
            self._name,
            padding=0,
            vertical_alignment = ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    alignment=ft.alignment.center,
                    expand=True,
                    gradient=ft.LinearGradient(
                        # colors=["#121212", "#2B2B2B"],
                        colors=self._theme.mode.BACKGROUND_GRADIENT,
                        rotation=8.5
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
                                    duration=500,
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