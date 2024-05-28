from view.patient.patient import PatientView
from controller.controller import Controller
from res.patient import PatientResource


class PatientController(Controller):

    def __init__(self, model):
        self.name = 'patient'
        self.subname = 'study'
        self.model = model
        self.view = PatientView(controller=self, model=self.model)

    def set_data(self):
        if self.view.patient_id:
            resp = PatientResource().get_row_by_id(self.name, self.view.patient_id)
            self.model.set_single(resp.data)
            resp = PatientResource().get_list_data(self.subname, self.view.patient_id)
            self.model.set_data(resp.data)
