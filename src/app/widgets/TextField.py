from typing import Literal
from flet import TextStyle, Colors, TextField, Icon, Control
from ...utils.layout import Layout

def textFeild(
    label: str,width: float | None = Layout.getWidth(0.19),
    max_length: int = None, icon: Icon = None,
    password: bool = False, can_reveal_password: bool = False,
    ref = None, hint_text: str = None,
    theme: Literal["white", "dark"] = "white",
    read_only: bool = False, value:str = None, 
    suffix: Control|None = None,
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
        )