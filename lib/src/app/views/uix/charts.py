import re
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
from scipy.interpolate import make_interp_spline
from os.path import dirname, abspath, join, exists
from os import makedirs
from typing import ClassVar

if matplotlib.get_backend().lower() not in ("agg", "module://matplotlib_inline.backend_inline"):
    matplotlib.use("Agg")

class Charts:
    SAVE_PATH = abspath(join(dirname(__file__), "../../../../../"))
    width_px: ClassVar[int] = 320
    height_px: ClassVar[int] = 80

    @classmethod
    def _save_fig(cls, fig: Figure, filename: str):
        cache_dir = join(Charts.SAVE_PATH, "storage", "temp", "charts")
        makedirs(cache_dir, exist_ok=True)
        path = join(cls.SAVE_PATH, "storage", "temp", "charts")
        file_path = join(cache_dir, filename)
        if not exists(file_path):
            fig.savefig(join(path, filename), transparent=True, bbox_inches='tight', pad_inches=0)
        return file_path

    @staticmethod
    def create_smooth_line_chart(x: np.ndarray, y: np.ndarray, title: str = "line_chart", width_px: int | None = None, height_px: int | None = None):
        width_px = width_px or getattr(Charts, "width_px", 250)
        height_px = height_px or getattr(Charts, "height_px", 50)

        # Criar interpolação suave
        x_suave = np.linspace(x.min(), x.max(), 300)
        spl = make_interp_spline(x, y, k=3)  # k=3 para spline cúbica
        y_suave = spl(x_suave)

        # Criar gráfico
        # eu quero uma proporção retangular
        plt.figure(figsize=(10, 5))  # Proporção retangular (largura > altura)
        # Converter pixels para polegadas (matplotlib usa polegadas)
        dpi = 100
        fig = plt.gcf()
        fig.set_size_inches(width_px / dpi, height_px / dpi) # type: ignore
        fig.set_dpi(dpi)
        plt.plot(x_suave, y_suave, color='white', linewidth=2.5)

        # Remover tudo
        plt.axis('off')
        plt.box(False)

        # Exibir
        plt.tight_layout()
        return Charts._save_fig(plt.gcf(), f'{title}.png')