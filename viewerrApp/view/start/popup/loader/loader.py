from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout


class Loader(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
