# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.

from model.start import StartModel
from controller.start import StartController

from model.patients_list import PatientsListModel
from controller.patients_list import PatientsListController

from model.study_list import StudyListModel
from controller.study_list import StudyListController

from model.patient import PatientModel
from controller.patient import PatientController

from model.study import StudyModel
from controller.study import StudyController

from model.series import SeriesModel
from controller.series import SeriesController

from model.photo import PhotoModel
from controller.photo import PhotoController

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
    "study_list": {
        "model": StudyListModel,
        "controller": StudyListController,
    },
    "patient": {
        "model": PatientModel,
        "controller": PatientController,
    },
    "study": {
        "model": StudyModel,
        "controller": StudyController,
    },
    "series": {
        "model": SeriesModel,
        "controller": SeriesController
    },
    "photo": {
        "model": PhotoModel,
        "controller": PhotoController
    }
}
