
from .pages.login import LoginPage
from .router.router import Router
from ..config.config import APP_NAME, VERSION
from ..utils.page import Page
from flet import ThemeMode

class App():
    def __init__(self) -> None:
        self.page = None
        self.router = Router()

    def __str__(self) -> str:
        return f"App(title: {APP_NAME}, version: {VERSION})"

    def settings(self) -> None:
        self.page = Page().get_page()
        # Configuração de estilos
        self.page.title = APP_NAME
        self.page.theme_mode = ThemeMode.DARK
        # Adição de páginas
        self.page.window.width = 1920
        self.page.window.height = 1080
        self.page.window.maximized = True
        self.page.views.append(LoginPage().get_view())
        self.page.update()
        
        # Atualização da página
        

    def run_app(self, page: Page) -> None:
        # Iniciando o singleton de page
        Page().set_page(page)
        # Aplicando configurações iniciais
        self.settings()

        
        