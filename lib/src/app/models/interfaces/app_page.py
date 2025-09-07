from abc import ABC, abstractmethod
from flet import View, Page

from lib.src.app.styles.theme import ThemeManager

class AppPage(ABC):
    _page: Page
    _name: str
    _theme: ThemeManager

    @abstractmethod
    def set_page(self, page: Page) -> None:
        '''Atribui a instancia principal do app para a página atual'''
        pass

    @abstractmethod
    def get_page(self) -> View:
        """Retorna a View que representa a página."""
        pass