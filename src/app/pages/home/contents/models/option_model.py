from flet import Ref, Container

from ...interface.model import ContentModel

class Option:
    _icon: str
    _title: str
    _ref: Ref[Container]
    _content: ContentModel

    def __init__(self, icon: str, title: str, ref: Ref[Container], content: ContentModel = None) -> None:
        self._icon = icon
        self._title = title
        self._ref = ref
        self._options = []
        self._content = content

    def __str__(self) -> str:
        return f"Option(icon: {self._icon}, tile: {self._title}, referencia: {self._ref})"

    def getIcon(self) -> str:
        return self._icon 

    def getTitle(self) -> str:
        return self._title
    
    def getRef(self) -> Ref[Container]:
        return self._ref

    def setSubMenu(self, lista: list):
        self._options = lista

    def getSubMenu(self) -> list:
        return self._options

    def getContent(self) -> ContentModel:
        return self._content