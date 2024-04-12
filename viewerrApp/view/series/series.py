from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivymd.uix.screen import MDScreen
from utility.observer import Observer
from view.series.components.list_item import InstanceListItem


class SeriesView(MDScreen, Observer):

    controller = ObjectProperty()

    model = ObjectProperty()

    manager_screens = ObjectProperty()

    series_id = StringProperty()
    patient_id = StringProperty()
    sex = StringProperty()
    birthday = StringProperty()
    study_id = StringProperty()
    study_date = StringProperty()
    study_description = StringProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)

    def model_is_changed(self):
        pass

    def on_enter(self):
        self.ids.instance_list_items.clear_widgets()
        self.generate_data()
        self.generate_and_added_items_to_list()

    def generate_data(self):
        # get data from database via patient_id
        self.patient_id = 'Patient'
        self.sex = 'male'
        self.birthday = '12/12/12'
        self.study_id = '0'
        self.study_date = '12/12/45'
        self.study_description = 'neuro crane'

    def generate_and_added_items_to_list(self):
        for i in range(15):
            instance_list_item = InstanceListItem(instance_id=f'{i}')
            self.ids.instance_list_items.add_widget(instance_list_item)

    def on_list_item_click(self, instance_id):
        pass
        # self.manager.transition.direction = "left"
        # self.manager_screens.get_screen("series").series_id = series_id
        # self.manager_screens.current = "series"
