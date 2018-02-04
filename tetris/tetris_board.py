import random


class TetrisBoard:

    total_positions = 4

    def __init__(self, rows, columns):
        self.shapes = []
        self.shape = None
        self.height = None
        self.width = None
        self.direction = None
        self.falling = None
        self.cleft = None
        self.cright = None
        self.rows = rows
        self.columns = columns

    def register_shapes(self, shape):
        self.shapes.append(shape)

    def choose_random_shape_and_direction(self):
        s = random.randint(0, len(self.shapes) - 1)
        shape = self.shapes[s]
        self.shape = shape.matrix
        self.height = shape.height
        self.width = shape.width
        self.direction = random.randint(0, self.total_positions - 1)

    def turn_clockwise(self, y, x, state_board):
        self.direction += 1
        if self.direction > 3:
            self.direction = 0

        if self.is_overlapping(y, x, state_board):
            self.direction -= 1
            if self.direction < 0:
                self.direction = 3

    def turn_anticlockwise(self, y, x, state_board):
        self.direction -= 1
        if self.direction < 0:
            self.direction = 3

        if self.is_overlapping(y, x, state_board):
            self.direction += 1
            if self.direction > 3:
                self.direction = 0

    def is_overlapping(self, y, x, state_board):
        ovl = 0
        for h in range(self.height):
            for w in range(self.width):
                if self.shape[h][w] == 1:
                    if self.direction == 0:
                        yt = y + h
                        xt = x + w
                    elif self.direction == 1:
                        yt = y + w
                        xt = x + ((self.height - 1) - h)
                    elif self.direction == 2:
                        yt = y + ((self.height - 1) - h)
                        xt = x + ((self.width - 1) - w)
                    elif self.direction == 3:
                        yt = y + ((self.width - 1) - w)
                        xt = x + h
                    if xt - 4 < 0:
                        ovl = 1
                    elif xt - 4 > (self.columns - 1):
                        ovl = 1
                    elif yt - 3 > 20:
                        ovl = 1
                    elif state_board[yt - 3][xt - 4] == 1:
                        ovl = 1
        return ovl

    def draw(self, y, x, drawer, state_board):
        self.cleft = 1
        self.cright = 1
        self.falling = 1
        for h in range(self.height):
            for w in range(self.width):
                if self.shape[h][w] == 1:
                    if self.direction == 0:
                        yt = y + h
                        xt = x + w
                    elif self.direction == 1:
                        yt = y + w
                        xt = x + ((self.height - 1) - h)
                    elif self.direction == 2:
                        yt = y + ((self.height - 1) - h)
                        xt = x + ((self.width - 1) - w)
                    elif self.direction == 3:
                        yt = y + ((self.width - 1) - w)
                        xt = x + h
                    drawer.draw(yt, xt)
                    if state_board[yt - 2][xt - 4] == 1:
                        self.falling = 0
                    if xt - 5 < 0:
                        self.cleft = 0
                    elif state_board[yt - 3][xt - 5] == 1:
                        self.cleft = 0
                    if xt - 3 > (self.columns - 1):
                        self.cright = 0
                    elif state_board[yt - 3][xt - 3] == 1:
                        self.cright = 0

    def update_state_board(self, y, x, state_board):
        for h in range(self.height):
            for w in range(self.width):
                if self.shape[h][w] == 1:
                    if self.direction == 0:
                        state_board[y + h - 3][x + w - 4] = 1
                    elif self.direction == 1:
                        state_board[y + w - 3][x + ((self.height - 1) - h) - 4] = 1
                    elif self.direction == 2:
                        state_board[y + ((self.height - 1) - h - 3)][x + ((self.width - 1) - w) - 4] = 1
                    elif self.direction == 3:
                        state_board[y + ((self.width - 1) - w) - 3][x + h - 4] = 1
        return state_board
