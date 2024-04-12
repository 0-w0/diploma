from kivymd.uix.list import ThreeLineListItem
from kivy.properties import StringProperty


class SeriesListItem(ThreeLineListItem):
    series_id = StringProperty()
