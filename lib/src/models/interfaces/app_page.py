from abc import ABC, abstractmethod
from flet import View, Page

class AppPage(ABC):
    _page: Page
    _name: str

    @abstractmethod
    def set_page(self, page: Page) -> None:
        '''Atribui a instancia principal do app para a página atual'''
        pass

    @abstractmethod
    def get_page(self) -> View:
        """Retorna a View que representa a página."""
        pass