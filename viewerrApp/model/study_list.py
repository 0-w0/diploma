import json


class StudyListModel:

    def __init__(self):
        self.study_description = {}
        path_to_study_description = "studies_all.json"
        if path_to_study_description:
            with open(path_to_study_description) as json_file:
                self.study_description = json.loads(json_file.read())
        self._observers = []

    def notify_observers(self):
        for observer in self._observers:
            observer.model_is_changed()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)
