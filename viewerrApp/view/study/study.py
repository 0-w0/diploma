from kivy.properties import StringProperty
from view.view import View
from view.study.components.list_item import SeriesListItem


class StudyView(View):
    patient_id = StringProperty()
    patient_name = StringProperty()
    sex = StringProperty()
    birthday = StringProperty()
    study_id = StringProperty()
    study_date = StringProperty()
    study_description = StringProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)

    def model_is_changed(self):
        self.controller.set_data()

    def on_enter(self):
        self.ids.series_list_items.clear_widgets()
        self.model_is_changed()
        self.generate_data()
        self.generate_and_added_items_to_list()

    def generate_data(self):
        self.patient_name = str(self.model.patient_description[0]['full_name'])
        self.patient_id = str(self.model.patient_description[0]['id'])
        self.sex = str(self.model.patient_description[0]['sex'])
        self.birthday = str(self.model.patient_description[0]['dob'])
        self.study_date = str(self.model.study_description[0]['date'])
        self.study_description = str(self.model.study_description[0]['description'])

    def generate_and_added_items_to_list(self):
        for series in self.model.series_description:
            try:
                series_list_item = SeriesListItem(series_id=str(series['id']))
                self.ids.series_list_items.add_widget(series_list_item)
            except ValueError:
                pass

    def on_list_item_click(self, series_id):
        self.manager.transition.direction = "left"
        self.manager_screens.get_screen("series").series_id = series_id
        self.manager_screens.current = "series"
