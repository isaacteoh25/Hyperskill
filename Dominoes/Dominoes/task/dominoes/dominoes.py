import random


class Domino:
    def __init__(self):
        self.cards = ([[a, b] for a in range(0, 7) for b in range(a, 7)])
        random.shuffle(self.cards)
        self.computer_pieces = []
        self.player_pieces = []
        self.snake = []
        self.status = ""

    def shuffle(self):
        random.shuffle(self.cards)

    def choice(self):
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card

    def form_pieces(self):
        double_domino = [-1, -1]
        for _ in range(7):
            computer_card = self.choice()
            player_card = self.choice()
            now_cards = [computer_card, player_card]
            for card in now_cards:
                if (card[0] == card[1]) and (card[0] > double_domino[0]):
                    double_domino = card
            self.computer_pieces.append(computer_card)
            self.player_pieces.append(player_card)
        if double_domino == [-1, -1]:
            self.cards += self.computer_pieces
            self.cards += self.player_pieces
            self.shuffle()
            return self.form_pieces()
        else:
            self.snake.append(double_domino)
            self.status = "player" if double_domino in self.computer_pieces else "computer"
            if double_domino in self.computer_pieces:
                self.computer_pieces.remove(double_domino)
            else:
                self.player_pieces.remove(double_domino)

    def print_computer(self):
        print(f'Computer pieces: {len(self.computer_pieces)}')

    def print_player(self):
        print('Your pieces:')
        for i, player_piece in enumerate(self.player_pieces):
            print(f'{i + 1}:{player_piece}')

    def print_snake(self):
        print(self.snake[0])

    def print_stock(self):
        # print(f'Stock pieces: {self.cards}')
        print(f'Stock size: {len(self.cards)}')

    def print_status(self):
        if self.status == "player":
            print("Status: It's your turn to make a move. Enter your command.")
        else:
            print("Status: Computer is about to make a move. Press Enter to continue...")


def main():
    game = Domino()
    game.form_pieces()
    print('======================================================================')
    game.print_stock()
    game.print_computer()
    game.print_snake()
    game.print_player()
    game.print_status()


main()