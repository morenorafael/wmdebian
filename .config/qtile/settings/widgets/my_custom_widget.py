from libqtile import bar, widget
from libqtile.widget import base


class MyCustomWidget(base._TextBox):

    def __init__(self, **config):
        super().__init__("", **config)
        # My widget's initialisation code here