from . import Shape


class Stick(Shape):

    @property
    def matrix(self):
        return [
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
