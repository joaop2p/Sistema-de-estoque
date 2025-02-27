from ...utils.page import Page
from ..pages.interface.model import ViewModel

class Router:
    def __init__(self) -> None:
        super().__init__()
        self.page = Page().get_page()

    def setView(self, page: ViewModel) -> None:
        new_view = page.get_view()
        self.page.views.append(new_view)
        self.page.go(new_view.route)
        self.page.update()

    def pop_view(self) -> ViewModel:
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)
        self.page.update()