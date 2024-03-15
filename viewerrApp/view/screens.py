# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.

from model.start import StartModel
from controller.start import StartController

screens = {
    # name screen
    "slider menu screen": {
        "model": StartModel,  # class of model
        "controller": StartController,  # class of controller
    },
}