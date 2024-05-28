from kivy.properties import StringProperty
from view.view import View
from view.series.components.list_item import InstanceListItem
from cnn.prediction import Prediction


class SeriesView(View):

    series_id = StringProperty()
    patient_id = StringProperty()
    patient_name = StringProperty()
    sex = StringProperty()
    birthday = StringProperty()
    study_id = StringProperty()
    study_date = StringProperty()
    study_description = StringProperty()
    prediction_result = []

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)

    def model_is_changed(self):
        self.controller.set_data()

    def on_enter(self):
        self.ids.instance_list_items.clear_widgets()
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
        self.study_id = str(self.model.study_description[0]['id'])

    def generate_and_added_items_to_list(self):
        for instance in self.model.instance_description:
            try:
                instance_list_item = InstanceListItem(instance_id=str(instance['id']))
                self.ids.instance_list_items.add_widget(instance_list_item)
            except ValueError:
                pass

    def on_list_item_click(self, instance_id=0):
        self.manager.transition.direction = "left"
        if self.manager_screens.get_screen("photo").series_id == self.series_id:
            self.manager_screens.get_screen("photo").download_flag = False
        else:
            self.manager_screens.get_screen("photo").download_flag = True
            self.manager_screens.get_screen("photo").series_id = self.series_id
        self.manager_screens.get_screen("photo").instance_id = instance_id
        self.manager_screens.current = "photo"

    def analyze_all(self):
        prediction = Prediction()
        self.prediction_result = \
            prediction.predict_url([instance['object_path'] for instance in self.model.instance_description])
        print(self.prediction_result)
        # copy = self.model.instance_description
        # copy = [obj[1] | {'analyzed': obj[0]} for obj in zip(self.prediction_result, copy)]


