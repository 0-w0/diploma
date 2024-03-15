from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from utility.observer import Observer


class StartView(MDScreen, Observer):
    """
    A class that implements a visual representation of the model data
    :class:`~Model.slider_menu_screen.SliderMenuScreenModel`.

    Implements a screen with slides of pizza varieties.
    """

    controller = ObjectProperty()
    """
    Controller object -
    :class:`~Controller.slider_menu_screen.SliderMenuScreenController`.

    :attr:`controller` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    model = ObjectProperty()
    """
    Model object - :class:`~Model.slider_menu_screen.SliderMenuScreenModel`.

    :attr:`model` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    manager_screens = ObjectProperty()
    """
    Screen manager object - :class:`~kivy.uix.screenmanager.ScreenManager`.

    :attr:`manager_screens` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)

    def model_is_changed(self):
        """
        The method that will be called on the observer when the model changes.
        """