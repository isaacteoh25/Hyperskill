import controller as ctrl


class Cell:
    """
    Represents one of the cells of the Board's grid.
        x: row position
        y: column position
        key: x and y concatenated
        mark: its printable character
    """

    def __init__(self, x, y, a_board):
        self.board = a_board
        self.x = x - 1
        self.y = y - 1
        self.key = str(x) + str(y)
        self.mark = '_' * len(str(a_board.rows * a_board.cols))
        self.visited = False

    def __str__(self):
        return self.mark

    def set_mark(self, mark):
        prefix = ' ' * (len(str(self.board.rows * self.board.cols)) - len(mark))
        self.mark = f"{prefix}{mark}"

    def adjacent_cells(self):
        """Return a set of Cells, possible to move to by Knight's move"""
        max_row = self.board.rows - 1
        max_col = self.board.cols - 1
        adjecent = {self.board.grid[self.x + r][self.y + c] for r in [-2, -1, 1, 2]
                    for c in [-2, -1, 1, 2] if 0 <= self.x + r <= max_row and
                    0 <= self.y + c <= max_col and abs(r) != abs(c)
                    and not self.board.grid[self.x + r][self.y + c].visited}
        return adjecent

    def has_possible_moves(self):
        return len(self.adjacent_cells()) != 0


class Board:
    """
    Represents the board of the Knight's Tour Puzzle.
    rows: number of rows across the y-axis
    cols: number of columns across the x-axis
    grid: 2D array (rows * cols)
    current: the current cell to make a move away from
    """

    def __init__(self, rows, cols):
        self.rows = rows  # vertical
        self.cols = cols  # horizontal
        self.grid = [[Cell(r, c, self) for c in range(1, cols + 1)] for r in range(1, rows + 1)]
        self.current = None

    def __str__(self):
        """
        Printable representation of the Board
        columns on horizontal axis position (left -> right)
        rows on vertical axis position (bottom -> up)
        """
        l_margin_space = len(str(self.rows))
        cell_width = len(self.grid[0][0].mark) + 1
        line = f'{" " * l_margin_space}--{"-" * (cell_width * self.cols)}-'
        output = line + '\n'
        for r in range(self.rows, 0, -1):
            l_row_space = len(str(self.rows)) - len(str(r))
            output += f'{" " * l_row_space}{r}| '
            for c in range(self.cols):
                cell = self.grid[r - 1][c]
                output += f'{cell} '
            output += '|\n'
        output += f'{line}\n'
        cols_footer = ' ' * (l_margin_space + 1)
        for c in range(1, self.cols + 1):
            num = str(c)
            cols_footer += ' ' * (cell_width - len(num)) + num
        output += cols_footer
        return output

    def get_cell(self, x, y):
        """Return a cell from the grid according to given coordinates"""
        return self.grid[y - 1][x - 1]

    def visit_cell(self, x, y):
        """Mark the cell of given coordinates as 'x' and visited"""
        cell = self.get_cell(x, y)
        cell.set_mark('x')
        cell.visited = True
        return cell

    def mark_possible_moves(self):
        """
        Mark the number of possible moves for each of the
        adjacent cells of the current cell
        """
        for cell in self.current.adjacent_cells():
            moves = str(len(cell.adjacent_cells()))
            cell.set_mark(moves)

    def update(self):
        """
        Unmark the number of possible moves for each of the
        adjacent cells of the current cell and set the current as visited.
        """
        self.current.set_mark('*')
        for cell in self.current.adjacent_cells():
            if not cell.visited:
                mark = '_' * len(str(self.rows * self.cols))
                cell.set_mark(mark)

    def count_visited(self):
        """Return how many cells have been visited"""
        counter = 0
        for row in self.grid:
            for cell in row:
                if cell.visited:
                    counter += 1
        return counter

    def is_solved(self):
        for row in self.grid:
            for cell in row:
                if not cell.visited:
                    return False
        return True


def result(gameboard):
    if gameboard.is_solved():
        print('What a great tour! Congratulations!')
    else:
        print('No more possible moves!')
        print(f'Your knight visited {gameboard.count_visited()} squares!')


if __name__ == '__main__':
    ctrl = ctrl.GameController()
    board = ctrl.input_board_dimensions()
    possible = True

    while possible:
        board.current = ctrl.input_coordinates()
        board.mark_possible_moves()
        possible = board.current.has_possible_moves()
        print(board)
        board.update()

    result(board)