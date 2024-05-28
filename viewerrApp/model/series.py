from model.model import Model


class SeriesModel(Model):

    def __init__(self):
        self._observers = []
        self.patient_description = {}
        self.study_description = {}
        self.series_description = {}
        self.instance_description = {}

    def set_data(self, study, patient, series, instance):
        self.set_study(study)
        self.set_patient(patient)
        self.set_series(series)
        self.set_instance(instance)

    def set_study(self, data):
        self.study_description = data

    def set_patient(self, data):
        self.patient_description = data

    def set_series(self, data):
        self.series_description = data

    def set_instance(self, data):
        self.instance_description = data
