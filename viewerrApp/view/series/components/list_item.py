from kivymd.uix.list import OneLineListItem
from kivy.properties import StringProperty


class InstanceListItem(OneLineListItem):
    instance_id = StringProperty()
