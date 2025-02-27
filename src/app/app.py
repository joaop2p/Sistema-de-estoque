from .services.database import Conect
from .pages.auth.login import LoginPage
from .router.router import Router
from ..config.config import APP_NAME, VERSION
from ..utils.page import Page
from flet import ThemeMode

class App():
    def __init__(self) -> None:
        self.page = None
        self.router = Router()
        self.conect = Conect()

    def __str__(self) -> str:
        return f"App(title: {APP_NAME}, version: {VERSION})"

    def settings(self) -> None:
        self.page = Page().get_page()
        # Configuração de estilos
        self.page.title = APP_NAME
        self.page.debug
        self.page.theme_mode = ThemeMode.DARK
        # Adição de páginas
        self.page.window.width = 1920
        self.page.window.height = 1080
        self.page.window.maximized = True
        self.page.fonts = {
            "sansation": "/fonts/sansation/Sansation_Regular.ttf"
            }
        self.page.update()

    def start(self) -> None:
        self.page.views.append(LoginPage(True).get_view())
        self.page.update()
        
    def run_app(self, page: Page) -> None:
        # Iniciando o singleton de page
        Page().set_page(page)
        # Aplicando configurações iniciais
        self.settings()
        self.start()

        
        