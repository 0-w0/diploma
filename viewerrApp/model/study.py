from model.model import Model


class StudyModel(Model):

    def __init__(self):
        self._observers = []
        self.patient_description = {}
        self.study_description = {}
        self.series_description = {}

    def set_data(self, study, patient, series):
        self.set_study(study)
        self.set_patient(patient)
        self.set_series(series)

    def set_study(self, data):
        self.study_description = data

    def set_patient(self, data):
        self.patient_description = data

    def set_series(self, data):
        self.series_description = data
