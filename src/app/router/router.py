from flet import View

from ...utils.singleton import SingletonMeta
from ..pages.model.model import ViewModel

class Router(metaclass = SingletonMeta):
    def __init__(self) -> None:
        self.pages = {}

    def setView(self, object: object, route: str) -> None:
        self.pages[route] = object
        
    def _getView(self, route: str) -> ViewModel:
        return self.pages[route]

    def getView(self, route: str) -> View:
        return self._getView(route).get_view()