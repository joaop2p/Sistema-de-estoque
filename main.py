import flet as ft
from src.app.app import App

class Main:
    def app(self):
        ft.app(App().run_app, name="Sistema de Estoques")


if __name__ == "__main__":
    main = Main()
    main.app()