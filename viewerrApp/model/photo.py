from model.model import Model


class PhotoModel(Model):
    def __init__(self):
        self._observers = []
        self.fill_list = []

    def set_data(self, data):
        self.fill_list = data
