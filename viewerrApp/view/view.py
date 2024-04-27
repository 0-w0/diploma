from kivymd.uix.screen import MDScreen
from utility.observer import Observer
from kivy.properties import ObjectProperty


class View(MDScreen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()
    manager_screens = ObjectProperty()

    def model_is_changed(self):
        pass
