from flet import Page as pg
from .singleton import SingletonMeta

class Page(metaclass=SingletonMeta):
    def __init__(self):
        self._page: pg = None

    def __str__(self):
        return self._page.title if self._page is not None else "Unamed"

    def set_page(self, page: pg):
        self._page = page
        
    def get_page(self):
        return self._page