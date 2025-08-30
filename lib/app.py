from flet import Page
from .src.config.app_config import AppConfig

class App:
    page: Page

    def __init__(self) -> None:
        self.app_config = AppConfig.get_instance()

    def _config_screen(self) -> None:
        self.app_config.set_app_settings(self.page)
        
    def run(self, page_instance: Page) -> None:
        self.page = page_instance
        self._config_screen()
