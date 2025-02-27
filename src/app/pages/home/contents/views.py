from .models.option_model import Option

class Views:
    def __init__(self):
        self._options: list[Option] = []
            
    def setOptions(self, options: list[Option]):
        self._options = options
        
    def getOptions(self) -> list[Option]:
        return self._options