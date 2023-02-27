from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name, rank, level):
        self.name = name
        self.rank = rank
        self.level = level
        super().__init__()

    @abstractmethod
    def fight(self):
        ...

    @abstractmethod
    def do_spell(self):
        ...

    def sing_song(self):
        print("No songs for me!")


# create a Wizard
class Wizard(Player):
    def fight(self):
        print("Magic with your lute.")

    def do_spell(self):
        print("Enchant everyone.")

