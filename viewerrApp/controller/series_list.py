from view.series_list.series_list import SeriesListView


class SeriesListController:

    def __init__(self, model):
        self.model = model  # Model.slider_menu_screen.SliderMenuScreenModel
        self.view = SeriesListView(controller=self, model=self.model)

    def get_view(self) -> SeriesListView:
        return self.view