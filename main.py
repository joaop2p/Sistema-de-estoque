from flet import app
from lib.app import App
from lib.utils.label_keys import LabelKey
from lib.utils.labels import Labels

if __name__ == "__main__":
    my_app = App()
    app(my_app.run, name=Labels.t(LabelKey.APP_TITLE))