from kivymd.uix.list import ThreeLineListItem
from kivy.properties import StringProperty


class StudyListItem(ThreeLineListItem):
    study_id = StringProperty()
