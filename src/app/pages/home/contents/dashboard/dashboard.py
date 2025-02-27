from ..views import Views
from .menu.overview_option import OverviewOption
from ..models.option_model import Option
from flet import Ref, Container, Icons

class Dashboard(Option, Views):
    def __init__(self):
        super().__init__(
            icon=Icons.BAR_CHART,
            title="Dashboards",
            ref=Ref[Container](),
            )
        self.setSubMenu(
            [OverviewOption()]
            )
    