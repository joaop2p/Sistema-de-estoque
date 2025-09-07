import flet as ft
from typing import Optional
from lib.src.app.styles.image import ImagesAssets
from lib.src.app.styles.theme import ThemeManager

class SideBar:
    _theme: ThemeManager
    _bar_controller: ft.Ref[ft.Container]
    _logo_controller: ft.Ref[ft.Container]
    _menu_controller: ft.Ref[ft.NavigationRail]
    _expanded: bool

    def __init__(self, theme: ThemeManager) -> None:
        self._theme = theme
        self._bar_controller = ft.Ref[ft.Container]()
        self._logo_controller = ft.Ref[ft.Container]()
        self._menu_controller = ft.Ref[ft.NavigationRail]()
        self._expanded = False

    def _hide_menu(self, e:ft.ControlEvent):
        # Checagens defensivas
        if (
            self._bar_controller.current is None
            or self._logo_controller.current is None
            or self._menu_controller.current is None
        ):
            return

        should_expand = e.data == 'true'
        if should_expand == self._expanded:
            return

        if should_expand:
            self._bar_controller.current.width = 200
            self._logo_controller.current.width = 200
            self._logo_controller.current.height = 150
            image = self._logo_controller.current.content
            if isinstance(image, ft.Image):
                image.src = (
                    ImagesAssets.DARK_THEME_LOGO
                    if self._theme.mode.name == 'dark'
                    else ImagesAssets.LIGHT_THEME_LOGO
                )
                image.scale = 1.2
                self._logo_controller.current.content = image
            # Mostrar labels via label_type quando expandido
            self._menu_controller.current.label_type = ft.NavigationRailLabelType.ALL
            self._expanded = True
        else:
            image = self._logo_controller.current.content
            self._bar_controller.current.width = 100
            self._logo_controller.current.width = 100
            self._logo_controller.current.height = 150
            if isinstance(image, ft.Image):
                image.src = ImagesAssets.ONLY_LOGO
                image.scale = 1
                self._logo_controller.current.content = image
            # Ocultar labels quando recolhido
            self._menu_controller.current.label_type = ft.NavigationRailLabelType.NONE
            self._expanded = False

        # Atualiza controles afetados
        self._bar_controller.current.update()

    def menu(self, page_height: Optional[float], options: dict) -> ft.Container:
        return ft.Container(
            bgcolor=self._theme.mode.MENU_COLOR,
            width=100,
            ref=self._bar_controller,
            height=page_height,
            on_hover=lambda e: self._hide_menu(e),
            animate=ft.Animation(300, ft.AnimationCurve.DECELERATE),
            alignment=ft.alignment.center,
            shadow=ft.BoxShadow(
                spread_radius=3,
                blur_radius=10,
                color=ft.Colors.with_opacity(0.05,ft.Colors.BLACK),
                offset=ft.Offset(3,0)
            ),
            content=self._menu(options)
        )
    def _menu(self, options: dict) -> ft.NavigationRail:
        return ft.NavigationRail(
            selected_index=0,
        ref=self._menu_controller,
        # Começa recolhido (sem labels); ao hover expandimos
        label_type=ft.NavigationRailLabelType.NONE,
            min_width=100,
            leading=ft.Container(
                        height=150,
                        width=100,
                        ref=self._logo_controller,
                        animate=ft.Animation(300, ft.AnimationCurve.DECELERATE),
                        alignment=ft.alignment.center,
                        content=ft.Image(
                            src=ImagesAssets.ONLY_LOGO,
                            fit=ft.ImageFit.CONTAIN,
                            scale=1.2
                        )
                    ),
            min_extended_width=200,
            bgcolor=self._theme.mode.MENU_COLOR,
            expand=True,
            selected_label_text_style=ft.TextStyle(color=self._theme.mode.BUTTON_COLOR, weight=ft.FontWeight.BOLD),
            unselected_label_text_style=ft.TextStyle(color=self._theme.mode.FONT_COLOR),
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.Icon(options[option]['icon']),
                    selected_icon=ft.Icon(options[option]['selected_icon']),
                    label=options[option].get('label', option.capitalize()),
                    # Guarda a chave para mapear o handler depois
                )
                for option in options
            ],
            on_change=lambda e:  print("Selected destination:", e.control.selected_index),
        )