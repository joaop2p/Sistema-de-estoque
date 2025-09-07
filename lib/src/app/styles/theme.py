from abc import ABC, abstractmethod
from typing import Any, Literal, Self

class Theme(ABC):
    name: Literal['light'] | Literal['dark']
    PRIMARY_GRADIENT: list[str]
    BACKGROUND_GRADIENT: list[str]
    TEXT_COLOR: str
    OBJECT_COLOR: Literal['light'] | Literal['dark']
    BUTTON_COLOR: str
    MENU_COLOR: str
    BODY_COLOR: str
    FONT_COLOR: str

class DarkTheme(Theme):
    name = 'dark'
    PRIMARY_GRADIENT = ["#1E1E1E","#383838"]
    BACKGROUND_GRADIENT = ["#1E1E1E","#383838"]
    OBJECT_COLOR = 'dark'
    MENU_COLOR = "#2D2D2D"
    BUTTON_COLOR = "#FFFFFF"
    BODY_COLOR = "#1E1E1E"
    FONT_COLOR = "#FFFFFF"

class LightTheme(Theme):
    name = 'light'
    PRIMARY_GRADIENT = ["#FFFFFF","#FFFFFF"]
    BACKGROUND_GRADIENT = ["#F8EBFD", "#EFE3F4"]
    OBJECT_COLOR = "light"
    MENU_COLOR = "#FFFFFF"
    BUTTON_COLOR = "#000000"
    BODY_COLOR = "#DDDBDB"
    FONT_COLOR = "#000000"

class ThemeManager:
    mode: Theme = DarkTheme()

    @classmethod
    def set_theme(cls, theme: Literal['dark'] | Literal['light']) -> None:
        cls.mode = DarkTheme() if theme == 'dark' else LightTheme()