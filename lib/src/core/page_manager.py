from typing import Self
from flet import Page, RouteChangeEvent

from lib.src.views.home import Home
from ..models.interfaces.app_page import AppPage

class PageManager:
    _page: Page
    _current_page: AppPage | None 
    _instance = None
    _routes: dict[str, AppPage] = {
        '/home': Home()
    }

    def __new__(cls) -> Self:
        if cls._instance is None:
            cls._instance = super(PageManager, cls).__new__(cls)
            cls._instance._current_page = None
        return cls._instance

    def set_page(self, page: Page):
        self._page = page
        self._page.on_route_change = self.change_page
        self._page.on_view_pop = self.view_pop

    def change_page(self, event: RouteChangeEvent) -> None:
        if event.data is None or event.data not in self._routes.keys():
            raise Exception
        new_view = self._routes[event.data]
        new_view.set_page(self._page)
        self._page.views.clear()
        self._page.views.append(new_view.get_page())
        self._page.update()

    def view_pop(self, view) -> None:
        self._page.views.pop()
        top_view = self._page.views[-1]
        if top_view.route:
            self._page.go(top_view.route)