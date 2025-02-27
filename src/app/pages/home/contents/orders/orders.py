from flet.core.container import Container
from flet import Ref, Icons
from ..models.option_model import Option


class Orders(Option):
    def __init__(self):
        super().__init__(
            icon = Icons.SHOPPING_BAG,
            title = "Pedidos",
            ref = Ref[Container]()
            )

