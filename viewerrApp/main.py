"""
The entry point to the application.

The application uses the MVC template. Adhering to the principles of clean
architecture means ensuring that your application is easy to test, maintain,
and modernize.

You can read more about this template at the links below:

https://github.com/HeaTTheatR/LoginAppMVC
https://en.wikipedia.org/wiki/Model–view–controller
"""
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


ViewerrApp().run()

