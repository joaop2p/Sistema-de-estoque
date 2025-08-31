from abc import ABC, abstractmethod
from typing import Any, Literal, Self

class Theme(ABC):
    name: Literal['light'] | Literal['dark']
    PRIMARY_GRADIENT: list[str]
    BACKGROUND_GRADIENT: list[str]
    TEXT_COLOR: str
    OBJECT_COLOR: Literal['light'] | Literal['dark']
    BUTTON_COLOR: str



class DarkTheme(Theme):
    name = 'dark'
    PRIMARY_GRADIENT = ["#1E1E1E","#383838"]
    BACKGROUND_GRADIENT = ["#1E1E1E","#383838"]
    OBJECT_COLOR = 'dark'
    
    # def __str__(self) -> Literal['light'] | Literal['dark']:
    #     return self._name

class LightTheme(Theme):
    name = 'light'
    PRIMARY_GRADIENT = ["#FFFFFF","#FFFFFF"]
    BACKGROUND_GRADIENT = ["#F8EBFD", "#EFE3F4"]
    OBJECT_COLOR = "light"

    # def __str__(self) -> str:
    #     return self._name

class ThemeManager:
    mode: Theme = DarkTheme()

    @classmethod
    def set_theme(cls, theme: Literal['dark'] | Literal['light']) -> None:
        cls.mode = DarkTheme() if theme == 'dark' else LightTheme()