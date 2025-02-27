from .contents.dashboard.contents.overview import Overview
from .contents.dashboard.menu.overview_option import OverviewOption
from .contents.orders.orders import Orders
from .contents.categorys.categorys import Categorys
from .contents.products.products import Products
from .contents.dashboard.dashboard import Dashboard
from .contents.views import Views
from ...widgets.otpion import option
from .interface.model import ContentModel
from .contents.profile.profile import Profile
import flet as ft
from ...router.router import Router
from ...models.user import User
from ....utils.layout import Layout
from ....utils.page import Page
from ..interface.model import ViewModel

class Home(ViewModel, Router, Views):
    content_area: ft.Ref[ft.Container]
        
    def __init__(self, *args,):
        self.page = Page().get_page()
        self.user = User()
        self.current_content: ContentModel = None

    def _chengedContent(self, target: ContentModel):
        if not isinstance(self.current_content, type(target)):
            self.current_content = target 
            self.content_area.current.content = target.getContent()
            self.page.update()

    def _houver(self, target: ft.Container | ft.Ref[ft.Container], event: ft.ControlEvent):
        houver = event.data == "true"
        for control in target.controls:
            if isinstance(control, ft.Text) or isinstance(control, ft.Icon):
                control.color = ft.Colors.GREY_700 if houver else ft.Colors.WHITE
        self.page.update()

    def _expandedMenu(self, ref: ft.Ref[ft.Container], event: ft.ControlEvent):  # noqa: F811
        houver = event.data == "true"
        ref.current.content.controls[1].height = None if houver else 0
        ref.current.content.controls[0].controls[-1].name = ft.Icons.ARROW_DROP_UP_ROUNDED if houver else ft.Icons.ARROW_DROP_DOWN_ROUNDED
        self._houver(ref.current.content.controls[0], event)
        self.page.update()

    def view(self):
        sair = ft.Ref[ft.Container]()
        profile = ft.Ref[ft.Container]()
        return ft.View(
            route="/home",
            controls=[
                ft.SafeArea(
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Container(
                                            content=ft.Text(
                                                value="Nome Da Empresa",
                                                size=27,
                                                color=ft.Colors.WHITE
                                                ),
                                            alignment=ft.alignment.center,
                                            padding=ft.padding.all(20)
                                            ),
                                        ft.Divider(color=ft.Colors.WHITE),
                                        ft.Container(
                                            content=ft.Row(
                                                controls=[
                                                    ft.Container(
                                                        content=ft.Container(
                                                            content=ft.Image(
                                                                src=self.user.getProfilePhoto(),
                                                                fit=ft.ImageFit.CONTAIN,
                                                                scale=1.5,
                                                                ),
                                                            width=50,
                                                            height=50,
                                                            border_radius=ft.border_radius.all(200),
                                                            ),
                                                        
                                                        alignment=ft.alignment.center,
                                                        ),
                                                    ft.Text(
                                                        value=self.user.getName().split()[0],
                                                        size=30,
                                                        color=ft.Colors.WHITE
                                                        )
                                                    ],
                                                alignment = ft.MainAxisAlignment.START,
                                                spacing=20
                                                ),
                                            alignment=ft.alignment.center,
                                            ref=profile,
                                            padding=ft.padding.all(20),
                                            on_click=lambda _: self._chengedContent(Profile()),
                                            on_hover=lambda e: self._houver(target=profile.current.content,event=e)
                                            ),
                                        ft.Divider(color=ft.Colors.WHITE),
                                        ft.Container(
                                            content=ft.Column(
                                                controls=[
                                                    ft.Container(
                                                        content=ft.Column(
                                                            controls=[
                                                                option(
                                                                    title=obj.getTitle(),
                                                                    icon=obj.getIcon()
                                                                    ),
                                                                ft.Container(
                                                                    content=ft.Column(
                                                                        controls=[
                                                                            ft.Container(
                                                                                content=ft.Column(
                                                                                    controls=[
                                                                                        option(
                                                                                            title=subobj.getTitle(),
                                                                                            icon=subobj.getIcon(),
                                                                                            is_list=False
                                                                                            ),
                                                                                    ]
                                                                                ),   
                                                                            ref=subobj.getRef(),
                                                                            on_hover= lambda e, x= subobj.getRef(): self._houver(x.current.content.controls[0], e),   
                                                                            on_click=lambda _, content = subobj.getContent() : self._chengedContent(content)                                                          
                                                                            ) for subobj in obj.getSubMenu()
                                                                        ]
                                                                    ),
                                                                    padding=ft.padding.all(20),
                                                                    height=0,
                                                                    animate_size=ft.Animation(400, ft.AnimationCurve.LINEAR),
                                                                    animate_rotation=ft.Animation(400, ft.AnimationCurve.LINEAR)
                                                                )
                                                            ]
                                                        ),
                                                        ref=obj.getRef(),
                                                        padding=ft.padding.all(10),
                                                        height=None,
                                                        on_hover= lambda e, r= obj.getRef(): self._expandedMenu(r,e),
                                                    ) for obj in self.getOptions()
                                                ]
                                            ),
                                            padding=ft.padding.all(20)
                                            ),
                                        ft.Divider(color=ft.Colors.WHITE),
                                        ft.Container(
                                            content=ft.Container(
                                                content=ft.Row(
                                                    controls=[
                                                        ft.Icon(
                                                            name=ft.Icons.LOGOUT,
                                                            size=25,
                                                            color=ft.Colors.WHITE,
                                                            ),
                                                        ft.Text(
                                                            value="Sair",
                                                            size=25,
                                                            color=ft.Colors.WHITE,
                                                            )
                                                        ],
                                                    ),
                                                alignment=ft.alignment.center,
                                                ),
                                            alignment=ft.alignment.bottom_center,
                                            padding=ft.padding.all(10),
                                            ref=sair,
                                            on_hover=lambda e: self._houver(target=sair.current.content.content, event=e),
                                            on_click= lambda _: (self.pop_view(), self.user.destroy())
                                            )
                                        ]
                                    ),
                                height=Layout.getHeight(1),
                                width=Layout.getWidth(0.17),
                                bgcolor="#6CA2F2",
                                padding=ft.padding.all(10),
                            ),
                            ft.AnimatedSwitcher(
                                content = ft.Container(
                                    content=ft.Container(),
                                    ref=self.content_area,
                                    height=Layout.getHeight(1),
                                    width=Layout.getWidth(1)-Layout.getWidth(0.17),
                                    expand=True,
                                    bgcolor=ft.Colors.WHITE
                                    ),
                                )
                            ],
                        spacing=0
                        )
                    )
                ],
            padding= ft.padding.all(0)
            )


    def get_view(self):
        self.content_area = ft.Ref[ft.Container]()
        self.setOptions([Dashboard(), Products(), Categorys(), Orders()])
        view = self.view()
        self.page.update()
        self._chengedContent(Overview(Dashboard.__name__))
        return view
        