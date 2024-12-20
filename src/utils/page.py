from flet import Page as pg
from .singleton import SingletonMeta

class Page(metaclass=SingletonMeta):
    def __init__(self):
        self.page: pg = None

    def __str__(self):
        return self.page.title if self.page is not None else "Unamed"

    def set_page(self, page: pg):
        self.page = page
        
    def get_page(self):
        return self.page