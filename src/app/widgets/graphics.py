import random
import flet as ft
from flet import Colors
import numpy as np
from time import sleep

def on_chart_event(e: ft.PieChartEvent, chart: ft.PieChart) -> None:
        for idx, section in enumerate(chart.sections):
            section.radius = (
                155 if idx == e.section_index else 150
            )
            section.update()
    

def Pier_Chart(ref: ft.Ref, data) -> ft.PieChart:
    colors = ["#4D9EF6", "#7E6BF2", "#6CA2F2", "#666975"]
    random.shuffle(colors)
    sections = [
        ft.PieChartSection(
            value=0,
            title=f"{item}",
            title_style=ft.TextStyle(
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE,
                shadow=ft.BoxShadow(color=ft.Colors.BLACK,spread_radius=0.5, blur_radius=1),
                ),
            color=color,
            radius=150,
            data={"value":value}
        )
        for item, color, value in zip(data.keys(),colors , data.values())
    ]
    total = sum(data.values())
    pier = ft.PieChart(
        ref=ref,
        sections=sections,
        # center_space_radius = 0,
        data=total,
        animate=ft.Animation(500, ft.AnimationCurve.EASE_OUT_SINE),
        on_chart_event=lambda e: on_chart_event(e, pier)
    )
    pier.sections.append(ft.PieChartSection(value= 0, color=ft.Colors.GREY))
    return pier

def _att_pierChart(ref: ft.Ref) -> None:
    chart: ft.PieChart = ref.current
    total_value = sum([section.data["value"] for section in chart.sections[:-1]])  
    for section in chart.sections[:-1]:
        target_value = section.data["value"] / total_value * 100
        t = section.title
        for _ in np.arange(0,target_value, 0.1):
            section.value += 0.1
            section.title = f"{t} {section.value :0.1f}%"
            section.update()
            sleep(0.001)
    chart.sections = chart.sections[:-1]
    chart.update()
