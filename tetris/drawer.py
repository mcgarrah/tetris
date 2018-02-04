import curses


class Drawer:

    FRAME_CHARACTER = '#'

    DRAWING_CHARACTER = '*'

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.screen = curses.initscr()
        self._init_curses()

    def draw_frame(self):
        self.screen.addstr(2, 3, self.FRAME_CHARACTER * (self.columns + 2))
        for n in range(3, self.rows + 3):
            self.screen.addstr(n, 3, self.FRAME_CHARACTER + ' ' * self.columns + self.FRAME_CHARACTER)
        self.screen.addstr(self.rows + 3, 3, self.FRAME_CHARACTER * (self.columns + 2))

    def draw(self, x, y, string=None):
        self.screen.addstr(x, y, string or self.DRAWING_CHARACTER)

    def get_input(self):
        return self.screen.getch()

    @staticmethod
    def delay():
        curses.halfdelay(1)

    def refresh(self):
        self.screen.refresh()

    def exit(self):
        self._exit_curses()

    @staticmethod
    def _init_curses():
        curses.noecho()
        curses.curs_set(0)

    @staticmethod
    def _exit_curses():
        curses.echo()
        curses.endwin()
