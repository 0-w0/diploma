from view.patient.patient import PatientView


class PatientController:

    def __init__(self, model):
        self.model = model  # Model.slider_menu_screen.SliderMenuScreenModel
        self.view = PatientView(controller=self, model=self.model)

    def get_view(self) -> PatientView:
        return self.view
