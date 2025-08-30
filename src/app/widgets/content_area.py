import flet as ft

def Content_area(title: str, content_ref: ft.Ref) -> ft.Container:
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text(
                        value = title,
                        text_align=ft.TextAlign.START,
                        style=ft.TextStyle(
                            size=29,
                            color=ft.Colors.WHITE,
                            weight=ft.FontWeight.BOLD
                            )                                            
                        ),
                    ),
                ft.Divider(color=ft.Colors.WHITE),
                ft.Container(
                    ref=content_ref,
                    content=ft.Container(
                        content=ft.ProgressRing(),
                        padding=ft.padding.all(100)
                        ),
                    # bgcolor=ft.Colors.WHITE,
                    # padding=ft.padding.all(100),
                    alignment=ft.alignment.center,
                    )
                ],
            spacing=20
            ),
        )