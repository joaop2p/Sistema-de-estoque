from flet import Ref, Icons, Container
from ..models.option_model import Option


class Products(Option):
    def __init__(self) -> None:
        super().__init__(
            icon = Icons.SHOPPING_BASKET_ROUNDED,
            title = "Produtos",
            ref = Ref[Container]()
            )
