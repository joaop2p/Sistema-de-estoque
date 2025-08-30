from flet import app, AppView
from lib.src.config.app_config import AppConfig
from lib.app import App

if __name__ == "__main__":
    config = AppConfig()
    my_app = App()
    app(my_app.run, name=config.app_title)