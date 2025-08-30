from os.path import exists
from flet import Page, Theme, ThemeMode
from typing import Any, Self
from configparser import ConfigParser

class AppConfig:
    app_title: str = 'Sistema de Estoque'
    _instance: Self
    _file_path: str = './config.ini'
    _initialized: bool = False
    _maximized: bool
    _theme: ThemeMode
    _config: ConfigParser

    def __init__(self) -> None:
        if AppConfig._initialized:
            return
        self._config = ConfigParser()
        self._load_configs()
        AppConfig._initialized = True

    def __new__(cls, *args: Any, **kwds: Any) -> Self:
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def set_app_settings(self, page_instance: Page) -> None:
        page_instance.title = self.app_title
        page_instance.window.maximized = self._maximized
        page_instance.theme_mode = self._theme
        page_instance.update()

    def _set_config(self):
        self._config['window_settings'] = {
            'maximized': str(self._maximized),
            'app_theme': self._theme.name.lower()
        }

    def _load_configs(self):
        if exists(self._file_path):
            self._config.read(self._file_path)
        self._maximized = self._config.getboolean('window_settings', 'maximized', fallback=True)
        self._theme = ThemeMode(value=self._config.get('window_settings', 'app_theme', fallback='dark'))
        self._set_config()
        self._save_file_config()

    def _save_file_config(self):
        self._set_config()
        with open(self._file_path, 'w') as f:
            self._config.write(f)
    @staticmethod
    def get_instance() -> "AppConfig":
        if AppConfig._instance is None:
            AppConfig()
        return AppConfig._instance