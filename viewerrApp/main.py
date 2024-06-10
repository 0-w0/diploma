import httpx
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
# from kivy.config import Config


Window.fullscreen = "auto"
Window.clearcolor = (243 / 255, 235 / 255, 230 / 255, 1)
# Config.set("graphics", "height", "1024")
# Config.set("graphics", "width", "1440")

from kivymd.app import MDApp

from view.screens import screens


class ViewerrApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)
        self.manager_screens = ScreenManager()

    def build(self):
        self.theme_cls.primary_palette = "DeepOrange"
        self.generate_application_screens()
        return self.manager_screens

    def generate_application_screens(self):
        for i, name_screen in enumerate(screens.keys()):
            model = screens[name_screen]["model"]()
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self.manager_screens
            self.manager_screens.add_widget(view)


try:
    ViewerrApp().run()
except httpx.ConnectError:
    print("bad getaway connection")

