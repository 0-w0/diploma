from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen


class StartLayout(Screen):
    pass


class SecondWindow(Screen):
    pass


# class StartLayout(Widget):
#     pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('view/start/start.kv')

class MyApp(App):
    def build(self):
        Window.fullscreen = "auto"
        Window.clearcolor = (243/255, 235/255, 230/255, 1)

        return kv


if __name__ == '__main__':
    MyApp().run()
