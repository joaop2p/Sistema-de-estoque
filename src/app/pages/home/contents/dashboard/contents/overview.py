from threading import Thread
from time import sleep
from typing import Literal
from weakref import ref
import flet as ft

from .overview_labels import SALES_GRAPHIC_PREDICTED, SALES_GRAPHIC_TITLE

from ......widgets.content_area import Content_area

from ......widgets.graphics import Pier_Chart, _att_pierChart

from .......utils.layout import Layout

from .......utils.page import Page

from ......models.user import User

from ....interface.model import ContentModel

class Overview(ContentModel):
    pier_chart: ft.Ref
    
    def __init__(self, main_title: str) -> None:
        self.user = User()
        self.page = Page().get_page()
        self.pier_chart = None
        self.main_title = main_title
        self.pier_chart_content_area = None

    def __str__(self) -> Literal['/overview']:
        return "/overview"

    def _att_char(self):
        sleep(5)
        print(self.pier_chart_content_area.current.width, self.pier_chart_content_area.current.height)
        self.pier_chart_content_area.current.content = Pier_Chart(ref=self.pier_chart,data=self._data())
        self.pier_chart_content_area.current.update()
        print(self.pier_chart_content_area.current.width, self.pier_chart_content_area.current.height)
        # sleep(5)
        _att_pierChart(self.pier_chart)

    def _data(self) -> dict:
        return {"cc": 50, "xx": 52, "tt": 73, "yy": 2}

    def getContent(self) -> ft.SafeArea:
        Thread(target=self._att_char).start()
        self.pier_chart = ft.Ref[ft.PieChart]()
        self.pier_chart_content_area = ft.Ref[ft.Container]()
        return ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content = ft.Text(
                            value=self.main_title,
                            text_align=ft.TextAlign.CENTER,
                            color=ft.Colors.WHITE,
                            style=ft.TextStyle(
                                weight=ft.FontWeight.BOLD,
                                size=40,
                                font_family="sansation"
                                ),
                            spans=[
                                ft.TextSpan(
                                    text="\tOverview",
                                    style = ft.TextStyle(
                                        size=25,
                                        color=ft.Colors.GREY_400
                                        )
                                    )
                                ]
                            ),
                        height=100,
                        alignment=ft.alignment.center,
                        gradient = ft.LinearGradient(
                            colors=[
                                "#00CCF5",
                                "#A868F7",
                                "#4670EB",
                                ],
                            rotation = 0.9
                            ),
                        shadow=ft.BoxShadow(
                            spread_radius=1,
                            blur_radius=5,
                            offset=ft.Offset(
                                x=1,
                                y=4,
                                ),
                            color=ft.Colors.with_opacity(
                                opacity=0.25,
                                color=ft.Colors.BLACK
                                )
                            ),
                        border_radius=ft.BorderRadius(
                            top_left=0,
                            top_right=0,
                            bottom_left=10,
                            bottom_right=10,
                            ),
                        ),
                    ft.Container(
                        content = ft.Column(
                            controls=[
                                ft.Container(
                                    content=ft.Row(
                                        controls=[
                                            ft.Container(
                                                content=ft.Column(
                                                    controls=[
                                                        ft.Container(
                                                            content=ft.CircleAvatar(
                                                                content=ft.Text("FF")
                                                                ), 
                                                            height=100,
                                                            width=100,
                                                            border_radius=ft.border_radius.all(100)
                                                            ),
                                                        ft.Container(
                                                            content=ft.Text(
                                                                value="0.000",
                                                                color=ft.Colors.GREY_600,
                                                                size=40
                                                                ),
                                                            padding=ft.padding.all(20)
                                                            ),
                                                        ft.Container(
                                                            content=ft.Text(
                                                                value="Context aqui",
                                                                color=ft.Colors.BLACK
                                                                ),
                                                            padding=ft.padding.all(20)
                                                            )
                                                        ]
                                                    ),
                                                height=300,
                                                width=300,
                                                bgcolor=ft.Colors.WHITE,
                                                border_radius=ft.border_radius.all(5),
                                                padding=ft.padding.all(20),
                                                shadow=ft.BoxShadow(
                                                    spread_radius=1,
                                                    blur_radius=5,
                                                    offset=ft.Offset(
                                                        x=0,
                                                        y=4,
                                                        ),
                                                    color=ft.Colors.with_opacity(
                                                        opacity=0.25,
                                                        color=ft.Colors.BLACK
                                                        )
                                                    ),
                                                )for _ in range(4)
                                            ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        spacing=100
                                        ),
                                    ),
                                ft.Row(
                                    controls=[
                                        ft.Container(
                                            content=Content_area(
                                                title=SALES_GRAPHIC_TITLE,
                                                content_ref=self.pier_chart_content_area
                                                ),
                                            height=500,
                                            padding=20,
                                            width=600,
                                            alignment=ft.alignment.center,
                                            border_radius=ft.border_radius.all(10),
                                            gradient = ft.LinearGradient(
                                                colors=[
                                                    ft.Colors.WHITE,
                                                    "#6F6DF0",
                                                    ],
                                                rotation = -8,
                                                ),
                                            shadow=ft.BoxShadow(
                                                    spread_radius=1,
                                                    blur_radius=5,
                                                    offset=ft.Offset(
                                                        x=0,
                                                        y=4,
                                                        ),
                                                    color=ft.Colors.with_opacity(
                                                        opacity=0.25,
                                                        color=ft.Colors.BLACK
                                                        )
                                                    ),
                                            ),
                                        ft.Container(
                                            content=Content_area(
                                                title=SALES_GRAPHIC_PREDICTED.title(),
                                                content_ref=None
                                                ),
                                            height=500,
                                            expand=True,
                                            padding=20,
                                            alignment=ft.alignment.center,
                                            bgcolor="#A868F7",
                                            border_radius=ft.border_radius.all(10),
                                            gradient = ft.LinearGradient(
                                                colors=[
                                                    ft.Colors.WHITE,
                                                    "#4670EB",
                                                    ],
                                                rotation = -8,
                                                ),
                                            shadow=ft.BoxShadow(
                                                    spread_radius=1,
                                                    blur_radius=5,
                                                    offset=ft.Offset(
                                                        x=0,
                                                        y=4,
                                                        ),
                                                    color=ft.Colors.with_opacity(
                                                        opacity=0.25,
                                                        color=ft.Colors.BLACK
                                                        )
                                                    ),
                                            )
                                        ],
                                    spacing=30
                                    )
                                ],
                            spacing=30
                            ),
                        height=Layout.getHeight(1),
                        alignment=ft.alignment.center,
                        padding=ft.padding.all(50),
                        )
                    ]
                )
            
            )