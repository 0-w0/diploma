from model.model import Model


class PatientModel(Model):

    def __init__(self):
        self._observers = []
        self.study_description = {}
        self.patient_description = []

    def set_data(self, data):
        self.study_description = data

    def set_single(self, data):
        self.patient_description = data
