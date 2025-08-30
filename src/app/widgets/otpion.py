from flet import Row, Icon, Text, Colors, Icons, FontWeight

def option(icon: str, title: str, is_list: bool = True) -> Row:
    return Row(
        controls=[
            Icon(
                name=icon,
                color=Colors.WHITE,
            ),
            Text(
                value=title,
                size=18,
                color=Colors.WHITE,
            ),
            Icon(
                name=Icons.ARROW_DROP_DOWN_ROUNDED,
                color=Colors.WHITE,
                visible=is_list
            ),
        ]
    )