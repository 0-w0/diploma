from view.patient.patient import PatientView


class PatientController:

    def __init__(self, model):
        self.model = model  # Model.slider_menu_screen.SliderMenuScreenModel
        self.view = PatientView(controller=self, model=self.model)

    def get_view(self) -> PatientView:
        # self.set_data()
        return self.view

    # def set_data(self):
    #     self.model.study_description = Resource().get_all_data('study')
