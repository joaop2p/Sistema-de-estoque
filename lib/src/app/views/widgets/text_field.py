from typing import Literal
from flet import TextStyle, Colors, Icon, Control
import flet as ft

class InputField:
    @staticmethod
    def default(
        label: str, icon: str | None = None, width: float | None = 300,
        max_length: int | None = None,
        password: bool = False, can_reveal_password: bool = False,
        ref = None, hint_text: str | None = None,
        theme: Literal["light", "dark"] = "dark",
        read_only: bool = False, value: str | None = None,
        suffix: Control | None = None, expand: bool = False,
        icon_color: str | None = None) -> ft.TextField:
        return ft.TextField(
            value=value,
            label=label,
            ref=ref,
            label_style=TextStyle(
                color=Colors.BLACK if theme == "light" else Colors.WHITE
            ),
            text_style=TextStyle(
                color=Colors.BLACK if theme == "light" else Colors.WHITE,
                ),
            border_color=Colors.BLACK if theme == "light" else Colors.WHITE,
            width=width,
            max_length=max_length,
            suffix=suffix,
            prefix_icon=Icon(
                name=icon,
                color= icon_color if icon_color is not None else Colors.BLACK if theme == "light" else Colors.WHITE
                ) if icon is not None else None,
            password=password,
            can_reveal_password=can_reveal_password,
            hint_text=hint_text,
            read_only=read_only,
            expand=expand
            )

    @staticmethod
    def search_field(
        label: str = "Search...",
        width: float | None = 300,
        color: str | None = None
    ) -> ft.TextField:
        return ft.TextField(
            label=label,
            height=50,
            text_size=14,
            label_style=TextStyle(
                color=ft.Colors.GREY,
            ),
            text_style=TextStyle(
                color=ft.Colors.GREY,
            ),
            border_color=Colors.TRANSPARENT,
            width=width,
            prefix_icon=Icon(
                name=ft.Icons.SEARCH,
                color= ft.Colors.GREY
                ),
            border_radius=10,
            bgcolor=color,
            )
    @staticmethod
    def drop_down(color: str | None = None, label: str | None = None) -> ft.Container:
        return ft.Container(
            # height=50,
            alignment=ft.alignment.center,
                content=ft.Dropdown(
                editable=True,
                label=label,
                label_style=TextStyle(
                    color=ft.Colors.GREY,
                ),
                text_style=TextStyle(
                    color=ft.Colors.GREY,
                ),
                # padding=0,
                # menu_height=40,
                # icon_size=14,
                text_size=14,
                border_color=Colors.TRANSPARENT,
                border_radius=10,
                width=300,
                filled=True,
                fill_color=color,
                options=[
                    ft.dropdown.Option("Red"),
                    ft.dropdown.Option("Green"),
                    ft.dropdown.Option("Blue"),
                ],
            # on_change=dropdown_changed,
            )
        )