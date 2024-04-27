from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivymd.uix.screen import MDScreen
from utility.observer import Observer
from view.patient.components.list_item import StudyListItem


class PatientView(MDScreen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()
    manager_screens = ObjectProperty()
    patient_id = StringProperty()
    sex = StringProperty()
    birthday = StringProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)

    def model_is_changed(self):
        pass

    def on_enter(self):
        self.ids.study_list_items.clear_widgets()
        self.generate_data()
        self.generate_and_added_items_to_list()

    def generate_data(self):
        # get data from database via patient_id
        self.sex = 'male'
        self.birthday = '12/12/12'

    def generate_and_added_items_to_list(self):
        for study in self.model.study_description.keys():
            study_list_item = StudyListItem(study_id=study)
            self.ids.study_list_items.add_widget(study_list_item)

    def on_list_item_click(self, study_id):
        self.manager.transition.direction = "left"
        self.manager_screens.get_screen("study").study_id = study_id
        self.manager_screens.current = "study"
