import abc


class Shape(metaclass=abc.ABCMeta):

    @property
    @abc.abstractmethod
    def matrix(self):
        raise NotImplementedError

    @property
    def height(self):
        _matrix = [[self.matrix[j][i] for j in range(4)] for i in range(4)]
        return self._get_max_length(_matrix)

    @property
    def width(self):
        return self._get_max_length(self.matrix)

    @staticmethod
    def _get_max_length(matrix):
        return max(list(map(sum, matrix)))
