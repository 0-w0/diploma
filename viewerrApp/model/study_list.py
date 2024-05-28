from model.model import Model


class StudyListModel(Model):

    def __init__(self):
        self.study_description = {}
        self._observers = []

    def set_data(self, data):
        self.study_description = data
