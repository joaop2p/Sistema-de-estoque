from abc import ABC, abstractmethod

from flet import Container, Page

from lib.src.app.styles.theme import ThemeManager

class ViewerPage(ABC):
    _theme: ThemeManager

    @abstractmethod
    def get_view(self) -> Container:
        pass

    # @abstractmethod
    # def set_page(self, page: Page):
    #     pass