from .drawer import Drawer
from .tetris_board import TetrisBoard
from .shapes import box, inverse_l, stick, outverse_j, z_shape


class TetrisManager:

    N_ROWS = 20
    N_COLUMNS = 20

    def __init__(self):
        self.state_matrix = self._init_state_matrix()
        self.drawer = Drawer(self.N_ROWS, self.N_COLUMNS)
        self.board = TetrisBoard(self.N_ROWS, self.N_COLUMNS)
        self.quit = False
        self.x = 0
        self.y = 0
        self._register_shapes()
        self.board.choose_random_shape_and_direction()

    def play(self):
        while not self.quit:
            self._reset_x_y()
            self.state_matrix = self._init_state_matrix()
            self.drawer.delay()
            self.drawer.draw(1, 3, 'TETRIS')
            self._draw_board()
            while True:
                self._get_input_and_apply_move()
                self._draw_board()
                if self.board.falling == 0:
                    self.state_matrix = self.board.update_state_board(self.y, self.x, self.state_matrix)
                    self._reset_x_y()
                    self.board.choose_random_shape_and_direction()
                    if self.board.is_overlapping(self.y, self.x, self.state_matrix):
                        break
                    self.y += self.board.falling
                    self._draw_shape()
                self._check_and_reset_completed_line()
            self._draw_game_over()
            self._get_closing_input()
            self.drawer.refresh()
        self.drawer.exit()

    def _draw_board(self):
        self.drawer.draw_frame()
        self.board.draw(self.y, self.x, self.drawer, self.state_matrix)

    def _check_and_reset_completed_line(self):
        for j in range(self.N_ROWS):
            if self.state_matrix[j] == [1 for _ in range(self.N_COLUMNS)]:
                for k in range(j, 0, -1):
                    self.state_matrix[k] = self.state_matrix[k - 1]
                    self.state_matrix[0] = [0 for _ in range(self.N_COLUMNS)]

    def _draw_game_over(self):
        self.drawer.refresh()
        self.drawer.draw(8, 3, "            ")
        self.drawer.draw(9, 3, " You Loose  ")
        self.drawer.draw(10, 3, "            ")
        self.drawer.draw(11, 3, " q to quit  ")
        self.drawer.draw(12, 3, "            ")
        self.drawer.draw(13, 3, " p to play  again")
        self.drawer.draw(14, 3, "            ")

    def _draw_shape(self):
        for j in range(self.N_ROWS):
            for i in range(self.N_COLUMNS):
                if self.state_matrix[j][i] == 1:
                    self.drawer.draw(j + 3, i + 4)

    def _init_state_matrix(self):
        return [
            [0 for _ in range(self.N_COLUMNS)] for _ in range(self.N_ROWS)] + [
            [1 for _ in range(self.N_COLUMNS)]
        ]

    def _reset_x_y(self):
        self.x = 8
        self.y = 3

    def _register_shapes(self):
        shapes = [box.Box(), inverse_l.InverseL(), stick.Stick(), outverse_j.OutverseJ(), z_shape.ZShape()]
        for shape in shapes:
            self.board.register_shapes(shape)

    def _get_closing_input(self):
        while 1:
            c = self.drawer.get_input()
            if c == ord('q'):
                self.quit = True
                break
            elif c == ord('p'):
                break

    def _get_input_and_apply_move(self):
        while True:
            c = self.drawer.get_input()
            if c == ord('w'):
                self.board.turn_clockwise(self.y, self.x, self.state_matrix)
                break
            elif c == ord('a'):
                self.x -= self.board.cleft
                break
            elif c == ord('d'):
                self.x += self.board.cright
                break
            elif c == ord('s'):
                self.board.turn_anticlockwise(self.y, self.x, self.state_matrix)
                break
