from view.series.series import SeriesView


class SeriesController:

    def __init__(self, model):
        self.model = model  # Model.slider_menu_screen.SliderMenuScreenModel
        self.view = SeriesView(controller=self, model=self.model)

    def get_view(self) -> SeriesView:
        return self.view
