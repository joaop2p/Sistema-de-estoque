from flet import SnackBar, Text, Colors

def error_warning(message: str) -> None:
    return SnackBar(
        open=True,
        content=Text(message, color=Colors.WHITE),
        bgcolor=Colors.RED,
        )