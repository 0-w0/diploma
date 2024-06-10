from view.view import View
from view.patients_list.components.list_item import PatientsListItem


class PatientsListView(View):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)

    def on_enter(self):
        self.ids.patients_list_items.clear_widgets()
        self.generate_and_added_items_to_list()

    def generate_and_added_items_to_list(self):
        for patient in self.model.patient_description:
            try:
                patient_list_item = PatientsListItem(patient_id=str(patient['id']),
                                                     patient_name=str(patient['full_name']),
                                                     birth_date=str(patient['dob']),
                                                     sex=str(patient['sex']))
                self.ids.patients_list_items.add_widget(patient_list_item)
            except ValueError:
                pass
            except IndexError:
                pass

    def on_list_item_click(self, patient_id):
        self.manager.transition.direction = "left"
        self.manager_screens.get_screen("patient").patient_id = patient_id
        self.manager_screens.current = "patient"
