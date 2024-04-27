from view.patients_list.patients_list import PatientsListView
from controller.controller import Controller


class PatientsListController(Controller):

    def __init__(self, model):
        self.name = 'patient'
        self.model = model
        self.view = PatientsListView(controller=self, model=self.model)
