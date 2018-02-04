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

    @property
    def height(self):
        return 1

    @property
    def width(self):
        return 4
