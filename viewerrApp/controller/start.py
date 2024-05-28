from view.start.start import StartView


class StartController:

    def __init__(self, model):
        self.model = model
        self.view = StartView(controller=self, model=self.model)

    def get_view(self) -> StartView:
        return self.view
