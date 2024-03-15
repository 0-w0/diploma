from view.start.start import StartView

class StartController:
    """
    The `SliderMenuScreenController` class represents a controller
    implementation. Coordinates work of the view with the model.

    The controller implements the strategy pattern. The controller connects
    to the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.slider_menu_screen.SliderMenuScreenModel
        self.view = StartView(controller=self, model=self.model)

    def get_view(self) -> StartView:
        return self.view
