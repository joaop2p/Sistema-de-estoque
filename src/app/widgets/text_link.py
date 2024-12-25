from flet import TextButton, Colors, ButtonStyle, TextStyle

def text_link(value_text: str, action) -> TextButton:
    return TextButton(
        text=value_text,
        style=ButtonStyle(
            overlay_color=Colors.TRANSPARENT,
            text_style = TextStyle(
                color= Colors.WHITE
                ),
            color= Colors.WHITE
            ),
        autofocus=False,
        on_click= action
        )