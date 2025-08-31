from os.path import exists
from flet import Page, Theme, ThemeMode
from typing import Any, Self
from configparser import ConfigParser

class AppConfig:
    _file_path: str = './config.ini'
    _initialized: bool = False
    _instance: Self
    _maximized: bool
    _theme: ThemeMode
    _config: ConfigParser
    _default_lan: str

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
        page_instance.window.maximized = self._maximized
        page_instance.theme_mode = self._theme
        page_instance.update()

    def _set_config(self):
        self._config['window_settings'] = {
            'maximized': str(self._maximized),
        }
        self._config['user_settings'] = {
            'app_theme': self._theme.name.lower(),
            'default_lan': self._default_lan
        }

    def _load_configs(self):
        if exists(self._file_path):
            self._config.read(self._file_path)
        self._maximized = self._config.getboolean('window_settings', 'maximized', fallback=True)
        self._theme = ThemeMode(value=self._config.get('window_settings', 'app_theme', fallback='dark'))
        self._default_lan = self._config.get('user_settings', 'default_lan', fallback='pt')
        self._set_config()
        self._save_file_config()

    def _save_file_config(self):
        self._set_config()
        with open(self._file_path, 'w') as f:
            self._config.write(f)

    @staticmethod
    def get_instance() -> "AppConfig":
        if not hasattr(AppConfig, "_instance") or AppConfig._instance is None:
            AppConfig()
        return AppConfig._instance
    
    @property
    def default_lang(self) -> str:
        return self._default_lan