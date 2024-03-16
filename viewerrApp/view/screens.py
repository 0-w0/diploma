# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.

from model.start import StartModel
from controller.start import StartController

from model.patients_list import PatientsListModel
from controller.patients_list import PatientsListController

from model.series_list import SeriesListModel
from controller.series_list import SeriesListController

from model.search import SearchModel
from controller.search import SearchController

screens = {
    # name screen
    "start": {
        "model": StartModel,  # class of model
        "controller": StartController,  # class of controller
    },
    "patients_list": {
        "model": PatientsListModel,
        "controller": PatientsListController,
    },
    "series_list": {
        "model": SeriesListModel,
        "controller": SeriesListController,
    },
    "search": {
        "model": SearchModel,
        "controller": SearchController,
    },
}