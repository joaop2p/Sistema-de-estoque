from flet import Page

from lib.utils.label_keys import LabelKey
from lib.utils.labels import Labels
from .src.config.app_config import AppConfig
from .src.core.page_manager import PageManager

class App:
    page: Page

    def __init__(self) -> None:
        self.app_config = AppConfig.get_instance()
        self.page_manager = PageManager()

    def _config_screen(self) -> None:
        self.app_config.set_app_settings(self.page)
        
    def run(self, page_instance: Page) -> None:
        self.page = page_instance
        self.page.title = Labels.t(LabelKey.APP_TITLE)
        self._config_screen()
        self.page_manager.set_page(self.page)
        self.page.go('/login')