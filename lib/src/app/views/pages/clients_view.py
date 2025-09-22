import asyncio
import random
from lib.src.app.controllers.client_api_controller import ClientApiController
from lib.src.app.models.client import Client
from lib.src.app.models.interfaces.viewer_page import ViewerPage
from lib.src.app.styles.theme import ThemeManager
import flet as ft
from lib.src.app.views.widgets.cards import ContactsCard
from lib.utils.labels.label_keys import LabelKey
from lib.utils.labels.labels import Labels
from lib.src.app.views.widgets.text_field import InputField
from faker import Faker

class ClientView(ViewerPage):
    _main_content_controller: ft.Ref[ft.Container]
    _theme: ThemeManager
    _cards: list[ft.Container]

    def __init__(self, page: ft.Page) -> None:
        super().__init__()
        self._theme = ThemeManager()
        self._page = page
        self._clients = []

    def _loading_screen(self):
        return ft.ProgressRing()
    
    async def _switch_to_clients_view(self):
        self._main_content_controller.current.content = self._loading_screen()
        self._page.update()
        self._cards = []
        clients = await ClientApiController.find_all()
        if clients:
            self._clients = clients
            for client in clients:
                card = ContactsCard(client).contacts_card(self._theme)
                setattr(card, "col", {"xs": 12, "md": 6, "lg": 4})
                self._cards.append(card)

            self._main_content_controller.current.content = ft.ResponsiveRow(
                controls=self._cards,
                columns=12,
                spacing=8,
                run_spacing=8,
                vertical_alignment=ft.CrossAxisAlignment.START,
                alignment=ft.MainAxisAlignment.START,
            )
            self._main_content_controller.current.alignment = ft.alignment.top_center
        else:
            self._main_content_controller.current.content = ft.Text(
                Labels.t(LabelKey.NO_CLIENTS_FOUND),
                color=self._theme.mode.FONT_COLOR,
                size=16,
            )
        self._main_content_controller.current.update()

    async def _fetch_clients(self) -> list[Client]:
        fake = Faker("pt_BR")
        await asyncio.sleep(1)
        # data = 
        return [
            Client(
                name=fake.name(),
                email=fake.email(),
                phone=fake.phone_number(),
                tag=random.randint(0, 2),
                created_at=fake.date_time(),
                updated_at=fake.date_time(),
                # photo=fake.image_url(),
                photo=None,
                status=random.randint(0, 2),
                id=fake.random_int()
            ) for _ in range(4)
        ]

    def get_view(self) -> ft.Container:
        self._main_content_controller = ft.Ref[ft.Container]()
        main_content = ft.Container(
            expand=True,
            alignment=ft.alignment.center,
            bgcolor=self._theme.mode.BODY_COLOR,
            ref=self._main_content_controller,
        )
        if not hasattr(self, "_load_task") or self._load_task is None:
            self._load_task = self._page.run_task(self._switch_to_clients_view)
        return ft.Container(
            padding=ft.padding.all(20),
            alignment=ft.alignment.center,
            expand=True,
            content=ft.Column(
                controls=[
                    ft.Container(
                        height=70,
                        content=ft.Row(
                            expand=True,
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.START,
                            controls=[
                                ft.Text(
                                    "Client View",
                                    size=30,
                                    weight=ft.FontWeight.BOLD,
                                    color=self._theme.mode.FONT_COLOR
                                ),
                                ft.Container(
                                    width=150,
                                    height=40,
                                    border_radius=5,
                                    bgcolor=self._theme.mode.SECOND_BUTTON_COLOR,
                                    on_click=lambda e: print('Add Product Clicked'),
                                    content=ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Icon(
                                                ft.Icons.ADD,
                                                color=ft.Colors.WHITE,
                                                size=20
                                            ),
                                            ft.Text(
                                                'Add Product',
                                                color=ft.Colors.WHITE,
                                                size=16,
                                                weight=ft.FontWeight.BOLD,
                                                font_family='sans-serif'
                                            )
                                        ]
                                    )
                                )
                            ]
                        ),
                    ),
                    ft.Container(
                        content=ft.Container(
                            height=70,
                            expand=True,
                            alignment=ft.alignment.center,
                            bgcolor=self._theme.mode.BODY_COLOR,
                            content=InputField.search_field(color=self._theme.mode.INPUT_COLOR, width=None),
                        )
                    ),
                    main_content
                ]
            )
        )