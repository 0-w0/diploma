from kivy.properties import StringProperty
from view.view import View
from view.patient.components.list_item import StudyListItem


class PatientView(View):
    patient_id = StringProperty()
    sex = StringProperty()
    birthday = StringProperty()
    full_name = StringProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)

    def model_is_changed(self):
        self.controller.set_data()

    def on_enter(self):
        self.ids.study_list_items.clear_widgets()
        self.model_is_changed()
        self.generate_data()
        self.generate_and_added_items_to_list()

    def generate_data(self):
        try:
            self.sex = self.model.patient_description[0]['sex']
            self.full_name = self.model.patient_description[0]['full_name']
            self.birthday = self.model.patient_description[0]['dob']
        except ValueError:
            pass
        except IndexError:
            pass

    def generate_and_added_items_to_list(self):
        for study in self.model.study_description:
            try:
                study_list_item = StudyListItem(study_id=str(study['id']))
                self.ids.study_list_items.add_widget(study_list_item)
            except ValueError:
                pass
            except IndexError:
                pass

    def on_list_item_click(self, study_id):
        self.manager.transition.direction = "left"
        self.manager_screens.get_screen("study").study_id = study_id
        self.manager_screens.current = "study"
