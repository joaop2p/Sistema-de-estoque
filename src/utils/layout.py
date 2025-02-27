from .page import Page

class Layout:
    @staticmethod
    def getHeight(value: float) -> float:
        return value * 1080
    
    @staticmethod
    def getWidth(value: float) -> float:
        return value * 1920

