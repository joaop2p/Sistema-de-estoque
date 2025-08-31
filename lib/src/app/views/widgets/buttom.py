from typing import Callable, Literal
from flet import Container, Colors, border, Text, TextStyle, FontWeight, Ref, ControlEvent, Animation, AnimationCurve 

class ButtomLogin:
    _ref: Ref[Container]
    _text: str
    _theme: Literal['dark'] | Literal['light']

    def __init__(self, text: str, theme: Literal['dark'] | Literal['light'], on_click: Callable, **kargs) -> None:
       self._text = text
       self._ref = Ref[Container]()
       self._theme=theme
       self._onclick = on_click
       self._args = kargs

    def _on_houve(self,event: ControlEvent, ref: Ref[Container]):
        if event.data == 'true':
            ref.current.scale = 1.1
        else:
            ref.current.scale = 1
        ref.current.update()

    @property
    def get(self) -> Container:
        return Container(
            ref=self._ref,
            on_hover= lambda e, ref=self._ref: self._on_houve(e, ref),
            border=border.all(width=1, color=Colors.BLACK if self._theme == 'light' else Colors.WHITE),
            padding=5,
            border_radius=5,
            on_click=lambda _: self._onclick(self._args),
            animate_scale=Animation(100, AnimationCurve.LINEAR),
            content=Text(
                self._text,
                style=TextStyle(
                    weight=FontWeight.BOLD,
                    color=Colors.BLACK if self._theme == 'light' else Colors.WHITE
                )
            ),
        )