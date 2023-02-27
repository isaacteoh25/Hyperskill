from itertools import product
from random import choice
from collections import Counter

class OccupiedCell(Exception): pass


class Field:
    coords = sorted(product(range(1, 4), repeat=2), key=lambda a: (- a[1], a[0]))

    def __init__(self, start=None):
        if start is None:
            self.cells = dict(zip(Field.coords, [' ' for n in range(9)]))
        else:
            self.cells = dict(zip(Field.coords, start))
        self.is_X_turn = bool(Counter(self.cells.values())[' '] % 2)
        self.state = 'Game not finished'

    def __str__(self):
        return ('---------\n'
                '| {} {} {} |\n'
                '| {} {} {} |\n'
                '| {} {} {} |\n'
                '---------').format(*self.cells.values())

    @property
    def free_cells(self):
        return [key for key in self.cells if self.cells[key] == ' ']

    def get_symbol(self, current=True):
        return ('X' if self.is_X_turn else 'O') if current else ('O' if self.is_X_turn else 'X')

    def evaluate(self, coord):
        return any(map(lambda a: len(set(a)) == 1 and ' ' not in set(a),
                       [[self.cells[(coord[0]), n] for n in range(1, 4)],
                        [self.cells[n, (coord[1])] for n in range(1, 4)],
                        [self.cells[n, n] for n in range(1, 4)],
                        [self.cells[n, 4 - n] for n in range(1, 4)]
                        ]))

    def update(self, coord, with_current_symbol=True, raise_OccupiedCell=True):
        if any(n < 1 or n > 3 for n in [*coord]):
            raise IndexError
        if raise_OccupiedCell and not self.cells[coord] == ' ':
            raise OccupiedCell

        symbol = self.get_symbol(with_current_symbol)
        self.cells[coord] = symbol
        self.is_X_turn = not self.is_X_turn
        if self.evaluate(coord):
            self.state = "{} wins".format(symbol)
            return True
        elif not Counter(self.cells.values())[' ']:
            self.state = 'Draw'
        return False


class Game:
    def __init__(self):
        self.players = []
        self.field = None
        self.main()

    def user_moves(self):
        while True:
            try:
                x, y = [int(n) for n in input('Enter the coordinates: (x y) > ').split()]
            except ValueError:
                print('You should enter numbers!')
                continue
            try:
                self.field.update((x, y))
            except IndexError:
                print('Coordinates should be from 1 to 3!')
                continue
            except OccupiedCell:
                print('This cell is occupied! Choose another one!')
                continue
            return True

    def make_random_move(self, coords=None):
        coord = choice(self.field.free_cells) if coords is None else choice(coords)
        self.field.update(coord)

    def bot_easy(self):
        print('Making move level "easy"')
        self.make_random_move()

    def bot_medium(self):
        print('Making move level "medium"')
        candidate_moves = self.get_candidate_moves()
        return self.make_random_move(candidate_moves) if candidate_moves else self.make_random_move()

    def bot_hard(self):
        print('Making move level "hard"')
        all_moves = self.minimax()
        if all_moves[1]:
            return self.make_random_move(all_moves[1])
        if all_moves[0]:
            return self.make_random_move(all_moves[0])
        if all_moves[-1]:
            return self.make_random_move(all_moves[-1])

    def get_candidate_moves(self, field=None):
        if field is None:
            field = self.field
        scenarios = {cell: Field(field.cells.values()) for cell in field.free_cells}
        return [cell for cell, field_obj in scenarios.items() if field_obj.update(cell)] or \
               [cell for cell, field_obj in scenarios.items() if field_obj.update(cell, True, False)]


    def minimax(self, field=None, deep=0):
        if field is None:
            field = self.field
        branches = {}
        for cell in field.free_cells:
            scenario = Field(field.cells.values())
            if scenario.update(cell):
                branches[cell] = -1 if deep % 2 else 1
            elif scenario.state.endswith('Draw'):
                branches[cell] = 0
            else:
                branches[cell] = self.minimax(scenario, deep + 1)
        if deep:
            return min(branches.values()) if deep % 2 else max(branches.values())
        else:
            return {
                1: [cell for cell in branches if branches[cell] == 1],
                0: [cell for cell in branches if branches[cell] == 0],
                -1: [cell for cell in branches if branches[cell] == -1]
            }


    @classmethod
    def player_move(cls, key):
        player_move = {
            'user': cls.user_moves,
            'easy': cls.bot_easy,
            'medium': cls.bot_medium,
            'hard': cls.bot_hard
        }
        return player_move[key]

    def play(self):
        print(self.field)
        for turn in range(9 - len(self.field.free_cells), 9):
            Game.player_move(self.players[turn % 2])(self)
            print(self.field)
            if not self.field.state == 'Game not finished':
                print(self.field.state)
                break

    def set_players(self, command):
        try:
            start_command, first_player, second_player = command.split()
            if all(player in ['user', 'easy', 'medium', 'hard'] for player in [first_player, second_player]):
                self.players = [first_player, second_player]
                return True
            else:
                return False
        except ValueError:
            return False

    def main(self):
        while True:
            command = input('Input command: > ')
            if command == 'exit':
                break
            elif self.set_players(command):
                self.field = Field()
                self.play()
            else:
                print('Bad parameters!')


if __name__ == '__main__':
    Game()

    # from itertools import product
    # from random import choice
    # from math import inf as infinity
    #
    #
    # class OccupiedCell(Exception):
    #     pass
    #
    #
    # class Field:
    #     coords = sorted(product(range(1, 4), repeat=2), key=lambda a: (- a[1], a[0]))
    #
    #     def __init__(self, start_status=' ' * 9):
    #         self.cells = dict(zip(Field.coords, start_status))
    #         self.is_O_turn = bool(len([value for value in self.cells.values() if not value == ' ']) % 2)
    #         self.state = 'Game not finished'
    #
    #     def __str__(self):
    #         return ('---------\n'
    #                 '| {} {} {} |\n'
    #                 '| {} {} {} |\n'
    #                 '| {} {} {} |\n'
    #                 '---------').format(*self.cells.values())
    #
    #     @property
    #     def free_cells(self):
    #         return [key for key in self.cells if self.cells[key] == ' ']
    #
    #     def get_symbol(self, current=True):
    #         return ('O' if self.is_O_turn else 'X') if current else ('X' if self.is_O_turn else 'O')
    #
    #     def evaluate_move(self, coord, symbol):
    #         field = self.cells.copy()
    #         field[coord] = symbol
    #         print([[field[(coord[0]), n] for n in range(1, 4)],
    #                [field[n, (coord[1])] for n in range(1, 4)],
    #                [field[n, n] for n in range(1, 4)],
    #                [field[n, -n + 4] for n in range(1, 4)]])
    #         if any(map(lambda a: len(set(a)) == 1 and ' ' not in set(a), [[field[(coord[0]), n] for n in range(1, 4)],
    #                                                                       [field[n, (coord[1])] for n in range(1, 4)],
    #                                                                       [field[n, n] for n in range(1, 4)],
    #                                                                       [field[n, -n + 4] for n in range(1, 4)]
    #                                                                       ])):
    #             return True
    #         else:
    #             return False
    #
    #     def update(self, coord):
    #         if any(n < 1 or n > 3 for n in [*coord]):
    #             raise IndexError
    #         if not self.cells[coord] == ' ':
    #             raise OccupiedCell
    #         symbol = self.get_symbol()
    #         self.cells[coord] = symbol
    #         if self.evaluate_move(coord, symbol):
    #             self.state = "{} wins".format(symbol)
    #         elif not [self.cells[coord] for coord in Field.coords if self.cells[coord] == ' ']:
    #             self.state = 'Draw'
    #         self.is_O_turn = not self.is_O_turn
    #
    #     def evaluate(self, state):
    #         """
    #         Function to heuristic evaluation of state.
    #         :param state: the state of the current board
    #         :return: +1 if the computer wins; -1 if the human wins; 0 draw
    #         """
    #         global score
    #         symbol1 = self.get_symbol()
    #         symbol2 = self.get_symbol(current=False)
    #         # if self.evaluate_move(coord, symbol1):
    #         if self.wins(state, symbol1):
    #             score = +1
    #         elif self.wins(state, symbol2):
    #             score = -1
    #         # elif not [self.cells[coord] for coord in Field.coords if self.cells[coord] == ' ']:
    #         else:
    #             score = 0
    #
    #         return score
    #
    #     def wins(self, state, player):
    #         """
    #         This function tests if a specific player wins. Possibilities:
    #         * Three rows    [X X X] or [O O O]
    #         * Three cols    [X X X] or [O O O]
    #         * Two diagonals [X X X] or [O O O]
    #         :param state: the state of the current board
    #         :param player: a human or a computer
    #         :return: True if the player wins
    #         """
    #         # player = self.get_symbol()
    #         # [field[(coord[0]), n] for n in range(1, 4)],
    #         # [field[n, (coord[1])] for n in range(1, 4)],
    #         # [field[n, n] for n in range(1, 4)],
    #         # [field[n, -n + 4] for n in range(1, 4)]
    #         win_state = [
    #             [state[1, 3], state[2, 3], state[3, 3]],
    #             [state[1, 2], state[2, 2], state[3, 2]],
    #             [state[1, 1], state[2, 1], state[3, 1]],
    #             [state[1, 1], state[1, 2], state[1, 3]],
    #             [state[2, 1], state[2, 2], state[2, 3]],
    #             [state[3, 1], state[3, 2], state[3, 3]],
    #             [state[1, 1], state[2, 2], state[3, 3]],
    #             [state[1, 3], state[2, 2], state[3, 1]],
    #         ]
    #
    #         if [player, player, player] in win_state:
    #             return True
    #         else:
    #             return False
    #
    #     def game_over(self, state):
    #         """
    #         This function test if the human or computer wins
    #         :param state: the state of the current board
    #         :return: True if the human or computer wins
    #         """
    #         symbol1 = self.get_symbol()
    #         symbol2 = self.get_symbol(current=False)
    #         return self.wins(state, symbol1) or self.wins(state, symbol2)
    #
    #     def minimax(self, fields, depth, current=True):
    #         """
    #         AI function that choice the best move
    #         :param coord: current state of the board
    #         :param depth: node index in the tree (0 <= depth <= 9),
    #         but never nine in this case (see iaturn() function)
    #         :param player: an human or a computer
    #         :return: a list with [the best row, best col, best score]
    #         """
    #         # symbol1 = self.get_symbol()
    #         if current:
    #             best = [-1, -1, -infinity]
    #         else:
    #             best = [-1, -1, +infinity]
    #
    #         if depth == 0 or self.game_over(fields):
    #             score = self.evaluate(fields)
    #             return [-1, -1, score]
    #
    #         for coord in self.free_cells:
    #             symbol = self.get_symbol()
    #             self.cells[coord] = symbol
    #             score = self.minimax(fields, depth - 1, not current)
    #             self.cells[coord] = ' '
    #             score[0], score[1] = coord
    #
    #             if current:
    #                 if score[2] > best[2]:
    #                     best = score  # max value
    #             else:
    #                 if score[2] < best[2]:
    #                     best = score  # min value
    #
    #         return best
    #
    #
    # class Game:
    #     def __init__(self):
    #         self.players = []
    #         self.field = None
    #         self.main()
    #
    #     def user_moves(self):
    #         while True:
    #             try:
    #                 x, y = [int(n) for n in input('Enter the coordinates: (x y) > ').split()]
    #             except ValueError:
    #                 print('You should enter numbers!')
    #                 continue
    #             try:
    #                 self.field.update((x, y))
    #             except IndexError:
    #                 print('Coordinates should be from 1 to 3!')
    #                 continue
    #             except OccupiedCell:
    #                 print('This cell is occupied! Choose another one!')
    #                 continue
    #             return True
    #
    #     def make_random_move(self):
    #         coord = choice(self.field.free_cells)
    #         self.field.update(coord)
    #
    #     def bot_easy(self):
    #         print('Making move level "easy"')
    #         self.make_random_move()
    #
    #     def bot_medium(self):
    #         print('Making move level "medium"')
    #         for coord in self.field.free_cells:
    #             if self.field.evaluate_move(coord, self.field.get_symbol()):
    #                 self.field.update(coord)
    #                 break
    #         else:
    #             for coord in self.field.free_cells:
    #                 if self.field.evaluate_move(coord, self.field.get_symbol(current=False)):
    #                     self.field.update(coord)
    #                     break
    #             else:
    #                 self.make_random_move()
    #
    #     def bot_hard(self):
    #         print('Making move level "hard"')
    #         depth = len(self.field.free_cells)
    #         if depth == 9:
    #             self.make_random_move()
    #         else:
    #             best = self.field.minimax(self.field.cells, depth)
    #             coords = (best[0], best[1])
    #             self.field.update(coords)
    #
    #     @classmethod
    #     def player_move(cls, key):
    #         player_move = {
    #             'user': cls.user_moves,
    #             'easy': cls.bot_easy,
    #             'medium': cls.bot_medium,
    #             'hard': cls.bot_hard
    #         }
    #         return player_move[key]
    #
    #     def play(self):
    #         print(self.field)
    #         for turn in range(9):
    #             Game.player_move(self.players[turn % 2])(self)
    #             print(self.field)
    #             if not self.field.state == 'Game not finished':
    #                 print(self.field.state)
    #                 break
    #
    #     def set_players(self, command):
    #         try:
    #             start_command, first_player, second_player = command.split()
    #             if all(player in ['user', 'easy', 'medium', 'hard'] for player in [first_player, second_player]):
    #                 self.players = [first_player, second_player]
    #                 return True
    #             else:
    #                 return False
    #         except ValueError:
    #             return False
    #
    #     def main(self):
    #         while True:
    #             command = input('Input command: > ')
    #             if command == 'exit':
    #                 break
    #             elif self.set_players(command):
    #                 self.field = Field()
    #                 self.play()
    #             else:
    #                 print('Bad parameters!')
    #
    #
    # if __name__ == '__main__':
    #     Game()