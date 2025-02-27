from ..contents.overview import Overview
from ...models.option_model import Option
from flet import Icons, Ref, Container

class OverviewOption(Option):
    def __init__(self):
        super().__init__(
            title="Overview",
            icon=Icons.INSERT_CHART,
            ref=Ref[Container](),
            content=Overview("Dashboard")
            )