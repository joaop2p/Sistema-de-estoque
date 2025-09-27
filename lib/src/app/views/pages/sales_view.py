from math import e
import numpy as np
import pandas as pd
from lib.src.app.models.interfaces.viewer_page import ViewerPage
from lib.src.app.styles.theme import ThemeManager
import flet as ft
from lib.src.app.views.uix.charts import Charts
from lib.src.app.views.widgets.text_field import InputField
from lib.utils.labels.label_keys import LabelKey
from lib.utils.labels.labels import Labels
import plotly.graph_objects as go
import plotly.express as px
from flet.plotly_chart import PlotlyChart

class SalesView(ViewerPage):
    _theme: ThemeManager

    def __init__(self) -> None:
        self._theme = ThemeManager()
        self._page = None

    #crie uma função que cria um gráfico em linha personalizado, não precisa ser necessariamente um gráfico real, pode ser uma linha de variação, ela precisa ser sua nas curvas
    # Não utilize o plotly.express, só crie uma linha com variações
    def create_custom_line_chart(self, df: pd.DataFrame) -> PlotlyChart:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df["dias"], y=df["vendas"], mode="lines+markers"))
        return PlotlyChart(figure=fig, expand=True)

    def get_view(self) -> ft.Container:
        # Crie um data frame com pandas com dados sintéticos que mostre o avanço de vendas ao longo da ultima semana
        df = pd.DataFrame({
            "dias": ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"],
            "vendas": [100, 200, 150, 300, 250, 400, 350]
        })
        path = Charts.create_smooth_line_chart(np.arange(len(df["dias"])), np.array(df["vendas"]), title="sales_line_chart")

        return ft.Container(
            padding=ft.padding.all(20),
            alignment=ft.alignment.center,
            expand=True,
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Row(
                        expand=True,
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.START,
                            controls=[
                                ft.Text(
                                    "Sales View",
                                    size=30,
                                    weight=ft.FontWeight.BOLD,
                                    color=self._theme.mode.FONT_COLOR
                                ),
                            ]
                        ),
                    ),
                    ft.Container(
                        content=ft.Container(
                            height=150,
                            expand=True,
                            alignment=ft.alignment.center,
                            bgcolor=self._theme.mode.BODY_COLOR,
                            content=ft.Row(
                                spacing=30,
                                controls=[
                                    ft.Container(
                                        width=800,
                                        # expand=True,
                                        content=ft.Row(
                                            controls=[
                                                ft.Container(
                                                    bgcolor=self._theme.mode.MENU_COLOR,
                                                    border_radius=ft.border_radius.all(10),
                                                    padding=ft.padding.all(10),
                                                    expand=True,
                                                    content=ft.Column(
                                                        controls=[
                                                            ft.Text('Sales Today', color=self._theme.mode.FONT_COLOR, size=16),
                                                            ft.Text('R$1.234,00', color=self._theme.mode.FONT_COLOR, size=24, weight=ft.FontWeight.BOLD),
                                                            ft.Image(src=path, fit=ft.ImageFit.CONTAIN, height=50, width=250)
                                                        ]
                                                    )
                                                ),
                                                ft.Container(
                                                    bgcolor=self._theme.mode.MENU_COLOR,
                                                    border_radius=ft.border_radius.all(10),
                                                    expand=True
                                                ),
                                                ft.Container(
                                                    bgcolor=self._theme.mode.MENU_COLOR,
                                                    border_radius=ft.border_radius.all(10),
                                                    expand=True
                                                ),
                                            ]
                                        )
                                    ),
                                    ft.Container(
                                        width=300,
                                        expand=True,
                                        # bgcolor=self._theme.mode.MENU_COLOR,
                                        # bgcolor=self._theme.mode.MENU_COLOR,
                                        content=ft.Container(
                                            bgcolor=self._theme.mode.MENU_COLOR,
                                            border_radius=ft.border_radius.all(10),
                                            expand=True
                                        )
                                    )
                                ]
                            ),
                        )
                    ),
                    ft.Container(
                        expand=True,
                        alignment=ft.alignment.center,
                        content=ft.Row(
                            spacing=30,
                            expand=True,
                            controls=[
                                ft.Container(
                                    alignment=ft.alignment.center,
                                    width=800,
                                    content=ft.Column(
                                        controls=[
                                            ft.Container(
                                                height=50,
                                                content=ft.Row(
                                                    controls=[
                                                        InputField.search_field(color=self._theme.mode.INPUT_COLOR, expand=True),
                                                        InputField.drop_down(color=self._theme.mode.INPUT_COLOR, label='Period', width=None),
                                                        InputField.drop_down(color=self._theme.mode.INPUT_COLOR, label='Status', width=None),
                                                    ]
                                                )
                                            ),
                                            ft.Container(
                                                expand=True,
                                                alignment=ft.alignment.center,
                                                content=ft.Text('Main Content Area', text_align=ft.TextAlign.CENTER, color=self._theme.mode.FONT_COLOR),
                                            )
                                        ]
                                    )
                                ),
                                ft.Container(
                                    alignment=ft.alignment.center,
                                    bgcolor=self._theme.mode.MENU_COLOR, 
                                    border_radius=ft.border_radius.all(10),
                                    # height=150,
                                    width=300,
                                    expand=True,
                                    content=ft.Text('Sales progress area', text_align=ft.TextAlign.CENTER, color=self._theme.mode.FONT_COLOR)
                                )
                            ]
                        )
                    )
                ]
            )
            #     controls=[
            #         ft.Row(
            #             controls=[
            #                 ft.Text(
            #                     'Sales Page',
            #                     size=30,
            #                     weight=ft.FontWeight.BOLD,
            #                     color=self._theme.mode.FONT_COLOR
            #                 )
            #             ]
            #         ),
            #         ft.Container(
            #             padding=20,
            #             expand=True,
            #             # height=100,
            #             # bgcolor='white',
            #             alignment=ft.alignment.top_center,
            #             content=ft.Row(
            #                 spacing=30,
            #                 alignment=ft.MainAxisAlignment.CENTER,
            #                 controls=[
            #                     ft.Container(
            #                         width=700,
            #                         content=ft.Column(
            #                             controls=[
            #                                 ft.Container(
            #                                     alignment=ft.alignment.center,
            #                                     # width=700,
            #                                     height = 150,
            #                                     # bgcolor=self._theme.mode.MENU_COLOR,
            #                                     # content=ft.Row(
            #                                     #     expand_loose=True,
            #                                     #     expand=True,
            #                                     #     controls=[
            #                                     #         ft.Container(
            #                                     #             bgcolor=self._theme.mode.MENU_COLOR,
            #                                     #             border_radius=ft.border_radius.all(10),
            #                                     #             # height=100,
            #                                     #             # width=200,
            #                                     #             expand=True
            #                                     #         ) for _ in range(3)
            #                                     #     ],
            #                                     #     # columns=12,
            #                                     #     spacing=15,
            #                                     #     run_spacing=8,
            #                                     #     vertical_alignment=ft.CrossAxisAlignment.CENTER,
            #                                     #     alignment=ft.MainAxisAlignment.CENTER,
            #                                     # )
            #                                     content=ft.Text('Summary Cards Area', text_align=ft.TextAlign.CENTER, color=self._theme.mode.FONT_COLOR)
            #                                 ),
            #                                 ft.Container(
            #                                     # width=700,
            #                                     height=50,
            #                                     # bgcolor='white',
            #                                     content=ft.Row(
            #                                         controls=[
            #                                             InputField.search_field(color=self._theme.mode.INPUT_COLOR, expand=True),
            #                                             InputField.drop_down(color=self._theme.mode.INPUT_COLOR, label='Period', width=None),
            #                                             InputField.drop_down(color=self._theme.mode.INPUT_COLOR, label='Status', width=None),
            #                                         ]
            #                                     )
            #                                 ),
            #                                 ft.Container(
            #                                     expand=True,
            #                                     alignment=ft.alignment.center,
            #                                     content=ft.Text('Main Content Area', text_align=ft.TextAlign.CENTER, color=self._theme.mode.FONT_COLOR),
            #                                 )
            #                             ]
            #                         ),
            #                     ),
            #                     ft.Container(
            #                         width=300,
            #                         expand=True,
            #                         # bgcolor=self._theme.mode.MENU_COLOR,
            #                         content=ft.Column(
            #                             controls=[
            #                                 ft.Container(
            #                                     alignment=ft.alignment.center,
            #                                     bgcolor=self._theme.mode.MENU_COLOR, 
            #                                     border_radius=ft.border_radius.all(10),
            #                                     height=150,
            #                                     # width=300,
            #                                     # expand_loose=True,
            #                                     expand=True,
            #                                     content=ft.Text('Side Area', text_align=ft.TextAlign.CENTER, color=self._theme.mode.FONT_COLOR)
            #                                 ),
            #                                 ft.Container(
            #                                     alignment=ft.alignment.center,
            #                                     # bgcolor=self._theme.mode.MENU_COLOR,
            #                                     border_radius=ft.border_radius.all(10),
            #                                     # height=150,
            #                                     # width=300,
            #                                     # expand_loose=True,
            #                                     expand=True,
            #                                     content=ft.Text('Sales progress area', text_align=ft.TextAlign.CENTER, color=self._theme.mode.FONT_COLOR)
            #                                 )
            #                             ]
            #                         )
            #                     )
            #                 ]
            #             )
            #         ),
                    
            #         #         controls=[
            #         #             ft.Column(
            #         #                 controls=[
            #         #                     ft.Container(
            #         #                         bgcolor='black',
            #         #                     )
            #         #                 ]
            #         #             )
            #         #         ]
            #         #     )
            #         # )
            #     ]
            # )
        )