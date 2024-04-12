from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from utility.observer import Observer
from view.patients_list.components.list_item import PatientsListItem


class PatientsListView(MDScreen, Observer):

    controller = ObjectProperty()

    model = ObjectProperty()

    manager_screens = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)

    def model_is_changed(self):
        pass

    def on_enter(self):
        self.ids.patients_list_items.clear_widgets()
        self.generate_and_added_items_to_list()

    def generate_and_added_items_to_list(self):
        for name in self.model.patient_description.keys():
            patient_list_item = PatientsListItem(patient_name=name,
                                                 birth_date=self.model.patient_description[name][0],
                                                 sex=self.model.patient_description[name][1])
            self.ids.patients_list_items.add_widget(patient_list_item)

    def on_list_item_click(self, patient_id):
        self.manager.transition.direction = "left"
        self.manager_screens.get_screen("patient").patient_id = patient_id
        self.manager_screens.current = "patient"
