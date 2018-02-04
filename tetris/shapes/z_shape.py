from . import Shape


class ZShape(Shape):

    @property
    def matrix(self):
        return [
            [1, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]

    @property
    def height(self):
        return 2

    @property
    def width(self):
        return 3