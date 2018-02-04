import abc


class Shape(metaclass=abc.ABCMeta):

    @property
    @abc.abstractmethod
    def matrix(self):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def height(self):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def width(self):
        raise NotImplementedError
