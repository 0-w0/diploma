from view.study.study import StudyView
from controller.controller import Controller
from res.study import StudyResource


class StudyController(Controller):

    def __init__(self, model):
        self.name = 'study'
        self.subname = 'patient'
        self.list_name = 'series'
        self.model = model
        self.view = StudyView(controller=self, model=self.model)

    def set_data(self):
        if self.view.study_id:
            resp = StudyResource().get_row_by_id(self.name, self.view.study_id)
            self.model.set_study(resp.data)
            resp = StudyResource().get_row_by_id(self.subname, self.model.study_description[0]['patient_id'])
            self.model.set_patient(resp.data)
            resp = StudyResource().get_list_data(self.list_name, self.view.study_id)
            self.model.set_series(resp.data)
