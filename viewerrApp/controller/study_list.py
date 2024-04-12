from view.study_list.study_list import StudyListView


class StudyListController:

    def __init__(self, model):
        self.model = model  # Model.slider_menu_screen.SliderMenuScreenModel
        self.view = StudyListView(controller=self, model=self.model)

    def get_view(self) -> StudyListView:
        return self.view
