from typing import Literal
from flet import TextStyle, Colors, TextField, Icon, Control

def text_Feild(
    label: str,icon: str|None =None, width: float | None = 300,
    max_length: int|None = None,
    password: bool = False, can_reveal_password: bool = False,
    ref = None, hint_text: str | None = None,
    theme: Literal["white", "dark"] = "white",
    read_only: bool = False, value:str | None = None, 
    suffix: Control|None = None, expand: bool = False, 
    icon_color: str | None = None) -> TextField:
    return TextField(
        value=value,
        label=label,
        ref=ref,
        label_style=TextStyle(
            color=Colors.WHITE if theme == "white" else Colors.BLACK
            ),
        text_style = TextStyle(
            color=Colors.WHITE if theme == "white" else Colors.BLACK,
            ),
        border_color=Colors.WHITE if theme == "white" else Colors.BLACK,
        width= width,
        max_length=max_length,
        suffix=suffix,
        prefix_icon=Icon(
            name=icon,
            color= icon_color if icon_color is not None else Colors.WHITE if theme == "white" else Colors.BLACK
            ) if icon is not None else None,
        password=password,
        can_reveal_password=can_reveal_password,
        hint_text=hint_text,
        read_only=read_only,
        expand=expand
        )