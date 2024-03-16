from view.patients_list.patients_list import PatientsListView


class PatientsListController:

    def __init__(self, model):
        self.model = model  # Model.slider_menu_screen.SliderMenuScreenModel
        self.view = PatientsListView(controller=self, model=self.model)

    def get_view(self) -> PatientsListView:
        return self.view
