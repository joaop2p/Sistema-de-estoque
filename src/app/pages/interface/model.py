from abc import ABC, abstractmethod
from flet import View

class ViewModel(ABC):
    @abstractmethod
    def get_view(self) -> View:
        pass