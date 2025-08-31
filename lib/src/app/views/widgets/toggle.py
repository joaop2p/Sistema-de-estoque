from flet import (
    Row, Text, alignment, Colors, TextStyle, FontWeight,
    border_radius, TextAlign, Container, MainAxisAlignment,
    Animation, AnimationCurve, Page, BoxShadow, Offset
)
from typing import Callable, Literal

from lib.src.app.styles import theme


class Toggle:

    
    def __init__(self, option_1_value: str, page: Page, option_2_value: str, on_click: Callable | None = None, theme: Literal['dark'] | Literal['light'] = 'dark'):
        self.option_1_state = True
        self.option_2_state = False
        self._theme = theme
        self.colors = {
            "selected": ["#D1D0D0", "#A8A8A8"] if theme =='dark' else ["#1F63E2", "#1F63E2"],
            "unselect": "#2B2B2B" if theme == 'dark' else "#FCF7F7"
        }
        self.option_1_button = self._create_option(option_1_value, self.option_1_state, True)
        self.option_2_button = self._create_option(option_2_value, self.option_2_state)
        self.page = page

        self.on_changed = on_click


    @property
    def current_option(self) -> str:
        """Retorna o valor da opção atualmente selecionada."""
        return (
            self.option_1_button.content.value # type: ignore
            if self.option_1_state
            else self.option_2_button.content.value # type: ignore
        )

    def _create_option(self, value: str, selected: bool, first: bool = False) -> Container:
        """Cria um botão de opção do switch."""
        match(self._theme):
            case 'light':
                color=Colors.WHITE if selected else Colors.BLACK
            case 'dark':
                color=Colors.BLACK if selected else Colors.WHITE
            case _:
                color=Colors.WHITE
        return Container(
            content=Text(
                value=value,
                text_align=TextAlign.CENTER,
                style=TextStyle(
                    color=color,
                    weight=FontWeight.BOLD
                )
            ),
            alignment=alignment.center,
            bgcolor=self.colors["selected"][0] if selected else self.colors["unselect"],
            height=100,
            width=250,
            animate=Animation(1000, AnimationCurve.BOUNCE_OUT),
            border_radius=border_radius.all(10),
            on_click=lambda _: self.on_click(first),
            disabled=selected 
        )

    def on_click(self, first: bool) -> None:
        """Alterna o estado do switch e atualiza os botões."""
        self.option_1_state = first
        self.option_2_state = not first
        self.update_buttons()

    def _update_button(self, button: Container, selected: bool, color: str) -> None:
        """Atualiza as propriedades visuais de um botão."""
        match(self._theme):
            case 'light':
                color=Colors.WHITE if selected else Colors.BLACK
            case 'dark':
                color=Colors.BLACK if selected else Colors.WHITE
            case _:
                color=Colors.WHITE
        button.bgcolor = self.colors["selected"][0] if selected else self.colors["unselect"]
        button.content.style.color = color# type: ignore
        button.disabled = selected
        button.update()

    def update_buttons(self) -> None:
        """Atualiza os dois botões e dispara o callback."""
        self._update_button(self.option_1_button, self.option_1_state, self.colors["selected"][0])
        self._update_button(self.option_2_button, self.option_2_state, self.colors["selected"][1])

        if callable(self.on_changed):
            self.on_changed()

    def get(self) -> Container:
        """Retorna o container principal do switch."""
        return Container(
            content=Row(
                controls=[self.option_1_button, self.option_2_button],
                alignment=MainAxisAlignment.CENTER,
                spacing=0
            ),
            width=500,
            height=50,
            bgcolor='#2B2B2B' if self._theme == 'dark' else "#FFFFFF",
            border_radius=border_radius.all(10),
            shadow=BoxShadow(
                spread_radius=5,
                blur_radius=15,
                color=Colors.with_opacity(0.1,Colors.BLACK),
                offset=Offset(0,1)
            )
        )
