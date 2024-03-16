from view.search.search import SearchView


class SearchController:

    def __init__(self, model):
        self.model = model  # Model.slider_menu_screen.SliderMenuScreenModel
        self.view = SearchView(controller=self, model=self.model)

    def get_view(self) -> SearchView:
        return self.view