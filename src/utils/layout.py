from .page import Page

class Layout:
    @staticmethod
    def getHeight(value: float) -> float:
        return value * Page().get_page().window.height
    
    @staticmethod
    def getWidth(value: float) -> float:
        return value * Page().get_page().window.width

