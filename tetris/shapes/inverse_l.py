from . import Shape


class InverseL(Shape):

    @property
    def matrix(self):
        return [
            [1, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
