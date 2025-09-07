from math import ceil

from pandas import DataFrame
from lib.src.app.models.interfaces.viewer_page import ViewerPage
from lib.src.app.styles.theme import ThemeManager
import flet as ft

from lib.src.app.views.widgets.text_field import InputField
from lib.utils.label_keys import LabelKey
from lib.utils.labels import Labels

class ProductView(ViewerPage):
    _theme: ThemeManager

    def __init__(self) -> None:
        super().__init__()
        self._theme = ThemeManager()
        self._page = None

        # Estado da paginação
        self._df: DataFrame | None = None
        self._page_size: int = 8
        self._current_page: int = 1 
        self._total_pages: int = 1

        # Referências de UI para atualização
        self._data_table: ft.DataTable | None = None
        self._page_info: ft.Text | None = None
        self._btn_prev: ft.IconButton | None = None
        self._btn_next: ft.IconButton | None = None

    def _build_rows_for_page(self, page_index: int) -> list[ft.DataRow]:
        """Monta as linhas da tabela para a página informada (1-based)."""
        assert self._df is not None
        start = (page_index - 1) * self._page_size
        end = start + self._page_size
        page_df = self._df.iloc[start:end]

        rows: list[ft.DataRow] = []
        for _, row in page_df.iterrows():
            rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(row["Name"])),
                        ft.DataCell(ft.Text(f"${row['Price']:.2f}")),
                        ft.DataCell(ft.Text(str(row["Stock"]))),
                        ft.DataCell(ft.Text(row["Category"])),
                        ft.DataCell(ft.Text(row["Status"])),
                    ]
                )
            )
        return rows

    def _update_table(self) -> None:
        """Atualiza a tabela e os controles de paginação para a página atual."""
        if not self._data_table or self._df is None:
            return

        self._total_pages = max(1, ceil(len(self._df) / self._page_size))
        # Garante limites
        self._current_page = max(1, min(self._current_page, self._total_pages))

        # Atualiza linhas da tabela
        self._data_table.rows = self._build_rows_for_page(self._current_page)
        self._data_table.update()

        # Atualiza label Página X/Y
        if self._page_info:
            self._page_info.value = f"Página {self._current_page}-{self._total_pages}"
            self._page_info.update()

        # Habilita/Desabilita botões
        if self._btn_prev:
            self._btn_prev.disabled = self._current_page <= 1
            self._btn_prev.update()
        if self._btn_next:
            self._btn_next.disabled = self._current_page >= self._total_pages
            self._btn_next.update()

    def _goto_page(self, new_index: int) -> None:
        self._current_page = new_index
        self._update_table()

    def get_view(self) -> ft.Container:
        # Dataset de exemplo
        self._df = DataFrame({
            "ID": [1, 2, 3],
            "Name": ["Product 1", "Product 2", "Product 3"],
            "Category": ["Category 1", "Category 2", "Category 3"],
            "Price": [10.0, 20.0, 30.0],
            "Stock": [100, 200, 300],
            "Status": ["Active", "Inactive", "Active"]
        })
        # Adiciona mais itens
        for i in range(4, 50):
            self._df.loc[len(self._df)] = {
                "ID": i,
                "Name": f"Product {i}",
                "Category": f"Category {i}",
                "Price": i * 10.0,
                "Stock": i * 100,
                "Status": "Active" if i % 2 == 0 else "Inactive"
            }

        # Calcula total de páginas
        self._total_pages = max(1, ceil(len(self._df) / self._page_size))
        self._current_page = 1

        # Colunas (ordem consistente com as células)
        columns = [
            ft.DataColumn(ft.Text("Name")),
            ft.DataColumn(ft.Text("Price")),
            ft.DataColumn(ft.Text("Stock")),
            ft.DataColumn(ft.Text("Category")),
            ft.DataColumn(ft.Text("Status")),
        ]

        # Tabela (linhas inicial: página 1)
        self._data_table = ft.DataTable(
            columns=columns,
            rows=self._build_rows_for_page(self._current_page),
            heading_row_color=self._theme.mode.DATA_TABLE_HEADER_COLOR,
            divider_thickness=1,
            data_row_color=self._theme.mode.DATA_TABLE_ROW_COLOR,
            expand_loose=True,
        )

        # Controles de navegação e label
        self._page_info = ft.Text(
            f"Página {self._current_page}-{self._total_pages}",
            color=self._theme.mode.FONT_COLOR,
            size=13,
            # weight=ft.FontWeight.BOLD
        )

        self._btn_prev = ft.IconButton(
            icon=ft.Icons.CHEVRON_LEFT,
            tooltip="Anterior",
            height=30,
            icon_size=13,
            width=30,
            style=ft.ButtonStyle(
                color=ft.Colors.GREY,
                bgcolor=self._theme.mode.TIRDY_BUTTON_COLOR,
                shape=ft.RoundedRectangleBorder(radius=5),
            ),
            on_click=lambda e: self._goto_page(self._current_page - 1),
            disabled=True,
        )

        self._btn_next = ft.IconButton(
            icon=ft.Icons.CHEVRON_RIGHT,
            tooltip="Próxima",
            height=30,
            width=30,
            icon_size=13,
            style=ft.ButtonStyle(
                color=ft.Colors.GREY,
                bgcolor=self._theme.mode.TIRDY_BUTTON_COLOR,
                shape=ft.RoundedRectangleBorder(radius=5),
            ),
            on_click=lambda e: self._goto_page(self._current_page + 1),
            disabled=self._total_pages <= 1,
        )

        return ft.Container(
            alignment=ft.alignment.center,
            expand=True,
            padding=ft.padding.all(20),
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Row(
                            expand=True,
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.START,
                            height=50,
                            controls=[
                                ft.Text(
                                    'Products',
                                    size=36,
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
                        height=70,
                        padding=ft.padding.all(10),
                        border_radius=5,
                        bgcolor=self._theme.mode.MENU_COLOR,
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                InputField.search_field(color=self._theme.mode.INPUT_COLOR),
                                InputField.drop_down(color=self._theme.mode.INPUT_COLOR, label='Category'),
                                InputField.drop_down(color=self._theme.mode.INPUT_COLOR, label='Order By'),
                            ]
                        )
                    ),
                    ft.ResponsiveRow(
                        expand=True,
                        controls=[
                            ft.Container(
                                bgcolor=self._theme.mode.MENU_COLOR,
                                expand=True,
                                border_radius=5,
                                content=self._data_table
                            )
                        ]
                    ),
                    # Navegação de páginas
                    ft.Container(
                        padding=ft.padding.only(top=10),
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.END,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                self._page_info,
                                self._btn_prev,
                                self._btn_next,
                            ]
                        )
                    )
                ]
            )
        )