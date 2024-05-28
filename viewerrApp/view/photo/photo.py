from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from view.view import View


class PhotoView(View):

    series_id = StringProperty(None, allownone=True)
    instance_id = NumericProperty(None, allownone=True)
    download_flag = True
    index = NumericProperty(None, allownone=True)
    path = StringProperty(None, allownone=True)

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)

    def on_enter(self):
        if self.instance_id:
            self.index = \
                next((index for (index, d) in enumerate(self.model.fill_list) if d["id"] == self.instance_id), 0)
        else:
            self.index = 0
        self.instance_id = None
        if self.download_flag:
            self.model_is_changed()
        if len(self.model.fill_list):
            self.ids.image.source = self.model.fill_list[self.index]['object_path']

    def model_is_changed(self):
        self.controller.set_data()

    def to_previous(self):
        self.index -= 1
        if self.index < 0:
            self.index = 0
        else:
            self.ids.image.source = self.model.fill_list[self.index]['object_path']

    def to_next(self):
        self.index += 1
        if self.index >= len(self.model.fill_list):
            self.index -= 1
        else:
            self.ids.image.source = self.model.fill_list[self.index]['object_path']

    def to_previous_screen(self):
        self.manager.transition.direction = "right"
        if self.series_id:
            self.manager_screens.get_screen("series").series_id = self.series_id
            self.manager_screens.current = "series"
        else:
            self.manager_screens.current = "start"
