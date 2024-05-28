import abc

class Model:
    @abc.abstractmethod
    def notify_observers(self):
        for observer in self._observers:
            observer.model_is_changed()

    @abc.abstractmethod
    def add_observer(self, observer):
        self._observers.append(observer)

    @abc.abstractmethod
    def remove_observer(self, observer):
        self._observers.remove(observer)

    @abc.abstractmethod
    def set_data(self, data):
        pass
