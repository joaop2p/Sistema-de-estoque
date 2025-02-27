from abc import ABC, abstractmethod
from flet import SafeArea

class ContentModel(ABC):
    @abstractmethod
    def getContent(self) -> SafeArea:
        pass