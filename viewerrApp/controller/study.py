from view.study.study import StudyView


class StudyController:

    def __init__(self, model):
        self.model = model  # Model.slider_menu_screen.SliderMenuScreenModel
        self.view = StudyView(controller=self, model=self.model)

    def get_view(self) -> StudyView:
        return self.view
