from view.series.series import SeriesView
from controller.controller import Controller
from res.series import SeriesResource


class SeriesController(Controller):

    def __init__(self, model):
        self.name = 'series'
        self.subname = 'study'
        self.subsubname = 'patient'
        self.list_name = 'object'
        self.model = model
        self.view = SeriesView(controller=self, model=self.model)

    def set_data(self):
        if self.view.series_id:
            resp = SeriesResource().get_row_by_id(self.name, self.view.series_id)
            self.model.set_series(resp.data)
            resp = SeriesResource().get_row_by_id(self.subname, self.model.series_description[0]['study_id'])
            self.model.set_study(resp.data)
            resp = SeriesResource().get_row_by_id(self.subsubname, self.model.study_description[0]['patient_id'])
            self.model.set_patient(resp.data)
            resp = SeriesResource().get_list_data(self.list_name, self.view.series_id)
            self.model.set_instance(resp.data)
