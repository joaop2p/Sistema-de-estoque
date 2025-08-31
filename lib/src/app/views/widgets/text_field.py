from typing import Literal
from flet import TextStyle, Colors, TextField, Icon, Control

def text_Feild(
    label: str,icon: str|None =None, width: float | None = 300,
    max_length: int|None = None,
    password: bool = False, can_reveal_password: bool = False,
    ref = None, hint_text: str | None = None,
    theme: Literal["light", "dark"] = "dark",
    read_only: bool = False, value:str | None = None, 
    suffix: Control|None = None, expand: bool = False, 
    icon_color: str | None = None) -> TextField:
    return TextField(
        value=value,
        label=label,
        ref=ref,
        label_style=TextStyle(
            color=Colors.BLACK if theme == "light" else Colors.WHITE
            ),
        text_style = TextStyle(
            color=Colors.BLACK if theme == "light" else Colors.WHITE,
            ),
        border_color=Colors.BLACK if theme == "light" else Colors.WHITE,
        width= width,
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