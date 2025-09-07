import flet as ft
import pandas as pd

# Exemplo de DataFrame
df = pd.DataFrame({
    "Produto": ["Teclado", "Mouse", "Monitor"],
    "Preço": [199.90, 99.90, 899.00],
    "Estoque": [35, 50, 12]
})

def main(page: ft.Page):
    page.title = "Tabela de Produtos"
    page.scroll = "auto"

    # Criando colunas da tabela
    columns = [
        ft.DataColumn(ft.Text("Produto")),
        ft.DataColumn(ft.Text("Preço")),
        ft.DataColumn(ft.Text("Estoque")),
    ]

    # Convertendo linhas do DataFrame para DataRow
    rows = []
    for _, row in df.iterrows():
        rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(row["Produto"]))),
                    ft.DataCell(ft.Text(f"R$ {row['Preço']:.2f}")),
                    ft.DataCell(ft.Text(str(row["Estoque"]))),
                ]
            )
        )

    # Montando DataTable
    tabela = ft.DataTable(
        columns=columns,
        rows=rows,
        border=ft.border.all(1, "white"),
        heading_row_color=ft.colors.BLUE_GREY_900,
        divider_thickness=1,
        data_row_color={"hovered": "blueGrey900"},
    )

    page.add(
        ft.Text("Produtos", size=20, weight="bold"),
        tabela
    )

ft.app(target=main)
