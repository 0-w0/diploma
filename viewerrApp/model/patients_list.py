import json

class PatientsListModel:

    def __init__(self):
        self.patient_description = {}
        path_to_patient_description = "patients.json"
        if path_to_patient_description:
            with open(path_to_patient_description) as json_file:
                self.patient_description = json.loads(json_file.read())
        self._observers = []

    def notify_observers(self):
        for observer in self._observers:
            observer.model_is_changed()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)
