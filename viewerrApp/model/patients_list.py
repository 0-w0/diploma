import json


class PatientsListModel:

    def __init__(self):
        self.patient_description = {}
        self._observers = []

    def notify_observers(self):
        for observer in self._observers:
            observer.model_is_changed()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def set_data(self, data):
        self.patient_description = data
