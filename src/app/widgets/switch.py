from flet import (
    Row, Text, alignment, Colors, TextStyle, FontWeight,
    border_radius, TextAlign, Container, MainAxisAlignment,
    Animation, animation
)
from ...utils.page import Page
from ...utils.layout import Layout

class Switch():
    def __init__(self, option_1_value: str, option_2_value: str, on_click = None):
        self.option_1_state = True
        self.option_2_state = False
        self.colors = {"selected": ["#00CCF5", "#A868F7"], "unselect": Colors.GREY_100}
        self.option_1_button = self._option(option_1_value, self.option_1_state, True)
        self.option_2_button = self._option(option_2_value, self.option_2_state)
        self.page = Page().get_page()
        self.on_chenged: callable = on_click

    @property
    def getCurrentOption(self) -> str:
        return self.option_1_button.content.value if self.option_1_state else self.option_2_button.content.value

    def _option(self, value: str, selected: bool, first: bool = False) -> Container:
        return Container(
            content=Text(
                value=value,
                text_align=TextAlign.CENTER,
                style=TextStyle(
                    color=Colors.WHITE if selected else Colors.BLACK,
                    weight=FontWeight.BOLD
                )
            ),
            alignment=alignment.center,
            bgcolor= self.colors["selected"][0] if selected else self.colors["unselect"],
            height=Layout.getHeight(0.05),
            width=Layout.getWidth(0.15) / 2,
            animate=Animation(400, animation.AnimationCurve.BOUNCE_IN),
            border_radius=border_radius.all(10),
            on_click=lambda e: self.on_click(first),
            disabled=first
        )

    def on_click(self, first: bool) -> None:
        self.option_1_state = first
        self.option_2_state = not first
        self.update_buttons()

    def update_buttons(self):
        self.option_1_button.bgcolor = self.colors["selected"][0] if self.option_1_state else self.colors["unselect"]
        self.option_1_button.content.style.color = Colors.WHITE if self.option_1_state else Colors.BLACK
        self.option_1_button.disabled = self.option_1_state
        self.option_1_button.update()

        self.option_2_button.bgcolor = self.colors["selected"][1] if self.option_2_state else self.colors["unselect"]
        self.option_2_button.content.style.color = Colors.WHITE if self.option_2_state else Colors.BLACK
        self.option_2_button.disabled = self.option_2_state
        self.option_2_button.update()
        self.on_chenged()

    def get(self):
        return Container(
            content=Row(
                controls=[
                    self.option_1_button,
                    self.option_2_button,
                ],
                alignment=MainAxisAlignment.CENTER,
                spacing=0
            ),
            width=Layout.getWidth(0.15),
            height=Layout.getHeight(0.05),
            bgcolor=Colors.WHITE,
            border_radius=border_radius.all(10)
        )
