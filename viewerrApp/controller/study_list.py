from view.study_list.study_list import StudyListView
from controller.controller import Controller


class StudyListController(Controller):

    def __init__(self, model):
        self.name = 'study'
        self.model = model
        self.view = StudyListView(controller=self, model=self.model)
