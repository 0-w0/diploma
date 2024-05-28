from view.view import View
from view.start.popup.loader.loader import Loader
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty
from kivy.uix.popup import Popup


class StartView(View):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)

    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def on_choose_dir(self):
        content = Loader(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        self.manager.transition.direction = "left"
        self.manager_screens.get_screen("photo").download_flag = True
        self.manager_screens.get_screen("photo").series_id = None
        self.manager_screens.get_screen("photo").instance_id = None
        self.manager_screens.get_screen("photo").path = path
        self.dismiss_popup()
        self.manager_screens.current = "photo"
    