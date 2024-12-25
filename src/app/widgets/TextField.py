from flet import TextStyle, Colors, TextField, Icon 
from ...utils.layout import Layout

def textFeild(label: str, max_length: int, icon: Icon = None, password: bool = False, can_reveal_password: bool = False, ref = None, hint_text: str = None) -> TextField:
    return TextField(
        label=label,
        ref=ref,
        label_style=TextStyle(
            color=Colors.WHITE
            ),
        text_style = TextStyle(
            color=Colors.WHITE,
            ),
        border_color=Colors.WHITE,
        width=Layout.getWidth(0.19),
        max_length=max_length,
        prefix_icon=Icon(name=icon, color=Colors.WHITE),
        password=password,
        can_reveal_password=can_reveal_password,
        hint_text=hint_text
        )