from flet.core.container import Container
from flet import Ref, Icons
from ..models.option_model import Option


class Categorys(Option):
    def __init__(self):
        super().__init__(
            icon = Icons.CATEGORY,
            title = "Categoria",
            ref = Ref[Container]()
            )
