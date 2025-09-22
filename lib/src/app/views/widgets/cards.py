import base64
import io
import os
import hashlib
import flet as ft
from typing import Optional
from lib.src.app.models.client import Client
from lib.src.app.styles.theme import ThemeManager
from faker import Faker
from string import ascii_uppercase

class ContactsCard:
    # @staticmethod

    def __init__(self, contact: Client) -> None:
        self.client = contact
        self._photo_b64: Optional[str] = None
        self._avatar: Optional[ft.CircleAvatar] = None
        self._photo_src: Optional[str] = None  # caminho local cacheado

    def _get_status(self):
        status = {
            0: {
                'color': ft.Colors.GREEN,
                'label': 'Active'
            },
            1: {
                'color': ft.Colors.RED,
                'label': 'Inactive'
            },
            2: {
                'color': ft.Colors.YELLOW,
                'label': 'Pending'
            }
        }
        font_color = ft.Colors.BLACK if self.client._tag == 2 else ft.Colors.WHITE
        return ft.Container(
            padding=ft.padding.all(5),
            # width=10,
            # width=40,
            border_radius=15,
            alignment=ft.alignment.center,
            bgcolor=status.get(self.client._tag, {}).get('color', ft.Colors.GREY),
            content=ft.Text(
                status.get(self.client._tag, {}).get('label', ''),
                style=ft.TextStyle(
                    color=font_color,
                    weight=ft.FontWeight.BOLD
                ),
                size=12,
            )
        )
    
    def _get_conection_status(self):
        status = {
            0: {
                'color': ft.Colors.GREEN,
                'label': 'Online'
            },
            1: {
                'color': ft.Colors.RED,
                'label': 'Offline'
            },
            2: {
                'color': ft.Colors.YELLOW,
                'label': 'Away'
            }
        }
        font_color = ft.Colors.BLACK if self.client._status == 2 else ft.Colors.WHITE
        return ft.Container(
            padding=ft.padding.all(5),
            # width=10,
            # width=40,
            border_radius=15,
            alignment=ft.alignment.center,
            bgcolor=status.get(self.client._status, {}).get('color', ft.Colors.GREY),
            content=ft.Text(
                status.get(self.client._status, {}).get('label', ''),
                style=ft.TextStyle(
                    color=font_color,
                    weight=ft.FontWeight.BOLD
                ),
                size=12,
            )
        )

    def _ensure_photo_src(self) -> Optional[str]:
        # Retorna caminho local (cache) para a foto, salvando se necessário
        if self._photo_src is not None:
            return self._photo_src

        data = getattr(self.client, "_photo", None)
        if not data:
            return None

        blob: Optional[bytes] = None
        try:
            if isinstance(data, (bytes, bytearray, memoryview)):
                blob = bytes(data)
            elif isinstance(data, str):
                s = data.strip()
                if s.startswith("data:"):
                    _, b64 = s.split(",", 1)
                    blob = base64.b64decode(b64)
                else:
                    # assume base64 puro
                    blob = base64.b64decode(s)
        except Exception:
            blob = None

        if not blob:
            return None

        # Detecta extensão simples por assinatura
        ext = ""
        if blob.startswith(b"\x89PNG\r\n\x1a\n"):
            ext = ".png"
        elif blob.startswith(b"\xff\xd8\xff"):
            ext = ".jpg"
        elif blob[:4] == b"RIFF" and blob[8:12] == b"WEBP":
            ext = ".webp"
        else:
            ext = ".img"  # genérico

        # Pasta de cache: <repo>/storage/temp/avatars
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../../"))
        cache_dir = os.path.join(base_dir, "storage", "temp", "avatars")
        os.makedirs(cache_dir, exist_ok=True)

        # Nome de arquivo estável por hash
        h = hashlib.sha256(blob).hexdigest()[:16]
        file_path = os.path.join(cache_dir, f"{h}{ext}")
        if not os.path.exists(file_path):
            try:
                with open(file_path, "wb") as f:
                    f.write(blob)
            except Exception:
                return None

        self._photo_src = file_path
        return self._photo_src

    def _normalize_photo_to_b64(self) -> Optional[str]:
        # Cache já calculado
        if self._photo_b64 is not None:
            return self._photo_b64

        data = getattr(self.client, "_photo", None)
        if not data:
            self._photo_b64 = None
            return None

        try:
            if isinstance(data, (bytes, bytearray, memoryview)):
                self._photo_b64 = base64.b64encode(bytes(data)).decode("ascii")
            elif isinstance(data, str):
                s = data.strip()
                if s.startswith("data:"):
                    # data URL -> pega a parte base64 depois da vírgula
                    _, b64 = s.split(",", 1)
                    self._photo_b64 = b64
                else:
                    # assume já ser base64 (evita recomputar)
                    # opcional: validar com base64.b64decode(s, validate=True)
                    self._photo_b64 = s
            else:
                self._photo_b64 = None
        except Exception:
            self._photo_b64 = None

        return self._photo_b64

    def _get_avatar(self):
        # Reusa o mesmo controle para evitar reenvio de base64 a cada update
        if self._avatar is not None:
            return self._avatar

        # Prefira arquivo local para evitar serialização de base64 em cada update
        src = self._ensure_photo_src()
        if not src:
            b64 = self._normalize_photo_to_b64()
        else:
            b64 = None

        if not (src or b64):
            self._avatar = ft.CircleAvatar(
                content=ft.Text(
                    (self.client._name or "?")[0].upper(),
                    color=ft.Colors.WHITE,
                    size=30,
                    weight=ft.FontWeight.BOLD,
                ),
                radius=30,
                bgcolor="blue",
            )
            return self._avatar

        if src:
            self._avatar = ft.CircleAvatar(
                radius=30,
                bgcolor="blue",
                content=ft.Image(
                    src=src,
                    fit=ft.ImageFit.COVER,
                    width=60,
                    height=60,
                    border_radius=30,
                ),
            )
        else:
            # Fallback base64 (apenas se não conseguimos salvar arquivo)
            self._avatar = ft.CircleAvatar(
                radius=30,
                bgcolor="blue",
                content=ft.Image(
                    src_base64=b64,  # type: ignore[arg-type]
                    fit=ft.ImageFit.COVER,
                    width=60,
                    height=60,
                    border_radius=30,
                ),
            )
        return self._avatar

    def _animation(self, e: ft.ControlEvent):
        # Altere apenas propriedades animáveis do controle já existente
        # Exemplo: animar scale do avatar sem reconstruir o conteúdo
        avatar = self._get_avatar()
        avatar.animate_scale = ft.Animation(200, ft.AnimationCurve.EASE_OUT)
        avatar.scale = 1.05 if (avatar.scale or 1) == 1 else 1
        avatar.update()

    def contacts_card(self, theme: ThemeManager) -> ft.Container:
        # Monte o card uma única vez e reutilize subcontroles
        avatar = self._get_avatar()
        fake = Faker("pt_BR")
        return ft.Container(
            expand=True,
            # animate_scale=ft.Animation(200, ft.AnimationCurve.EASE_IN_OUT),
            # on_hover=lambda e: self._animation(e),
            content=ft.Card(
                expand=True,
                height=160,
                color= theme.mode.CARD_COLOR,
                content=ft.Container(
                    expand=True,
                    alignment=ft.alignment.center,
                    padding=ft.padding.all(10),
                    content=ft.Column(
                        spacing=2,
                        controls=[
                            ft.Row(
                                controls=[
                                    avatar,
                                    ft.Container(
                                        width=10,
                                        # bgcolor='white',
                                        expand=True,
                                        content=ft.Column(
                                            spacing=2,
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            horizontal_alignment=ft.CrossAxisAlignment.START,
                                            controls=[
                                                ft.Text(
                                                    self.client._name,
                                                    size=18,
                                                    weight=ft.FontWeight.BOLD,
                                                    color=theme.mode.FONT_COLOR
                                                ),
                                                ft.Row(
                                                    # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                    controls=[
                                                        self._get_status(),
                                                        self._get_conection_status()
                                                    ]
                                                )
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            ft.Divider(height=5, color=theme.mode.BODY_COLOR),
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Icon(
                                            ft.Icons.PHONE,
                                            color=theme.mode.FONT_COLOR
                                        ),
                                        ft.Text(
                                            self.client._phone,
                                            size=14,
                                            color=theme.mode.FONT_COLOR
                                        )
                                    ]
                                )
                            ),
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Icon(
                                            ft.Icons.EMAIL,
                                            color=theme.mode.FONT_COLOR
                                        ),
                                        ft.Text(
                                            self.client._email,
                                            size=14,
                                            color=theme.mode.FONT_COLOR
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            )
        )