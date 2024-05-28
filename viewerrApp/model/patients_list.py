from model.model import Model


class PatientsListModel(Model):

    def __init__(self):
        self.patient_description = {}
        self._observers = []

    def set_data(self, data):
        self.patient_description = data
