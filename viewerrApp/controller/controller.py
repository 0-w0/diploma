import abc
from res.resource import Resource
from view.view import View


class Controller:
    @abc.abstractmethod
    def set_data(self):
        resp = Resource().get_all_data(self.name)
        self.model.set_data(resp.data)

    @abc.abstractmethod
    def get_view(self) -> View:
        self.set_data()
        return self.view
