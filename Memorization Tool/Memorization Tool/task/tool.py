# #sol 1
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import sessionmaker
#
# engine = create_engine('sqlite:///flashcard.db?check_same_thread=False')
#
# Base = declarative_base()
#
#
# class MyClass(Base):
#     __tablename__ = 'flashcard'
#     id = Column(Integer, primary_key=True)
#     question = Column(String)
#     answer = Column(String)
#     box_number = Column(Integer)
#
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()
#
# def into_choice(word):
#     choice = input(f'{word}: ')
#     if not choice:
#         return into_choice(word)
#     else:
#         return choice
#
#
# def into_practice(select):
#     num = input('press "d" to delete the flashcard:\npress "e" to edit the flashcard:\n')
#     if num == 'd':
#         session.delete(select)
#         session.commit()
#     elif num == 'e':
#         quest = input(f'current question: {select.question}\nplease write a new question: ')
#         select.question = quest
#         answ = input(f'current answer: {select.answer}\nplease write a new answer: ')
#         select.answer = answ
#         session.commit()
#     else:
#         print(f'{num} is not an option')
#
#
# def func_boxes(select):
#     num = input('press "y" if your answer is correct:\npress "n" if your answer is wrong:\n')
#     if num == 'y':
#         select.box_number = select.box_number + 1
#         session.commit()
#         if select.box_number >= 2:
#             session.delete(select)
#             session.commit()
#     elif num == 'n':
#         select.box_number = 0
#         session.commit()
#     else:
#         print(f'{num} is not an option')
#
#
#
# def add_flash():
#     while True:
#         num = input('1. Add a new flashcard\n2. Exit\n')
#         if num == '1':
#             question = into_choice('Question')
#             answer = into_choice('Answer')
#             box_num = 0
#             new_data = MyClass(question=question, answer=answer, box_number=box_num)
#             session.add(new_data)
#             session.commit()
#             return add_flash()
#         elif num == '2':
#             return main_menu()
#         else:
#             print(f'{num} is not an option')
#
#
# def practice_flash():
#     my_table = session.query(MyClass).all()
#     if my_table:
#         for i in range(len(my_table)):
#
#             print(f'Question: {my_table[i].question}')
#             num = input('press "y" to see the answer:\npress "n" to skip:\npress "u" to update:\n')
#             if num == 'y':
#                 print(f'Answer: {my_table[i].answer}')
#                 func_boxes(my_table[i])
#             elif num == 'n':
#                 func_boxes(my_table[i])
#                 continue
#             elif num == 'u':
#                 into_practice(my_table[i])
#             else:
#                 print(f'{num} is not an option')
#     else:
#         print('There is no flashcard to practice!')
#         main_menu()
#
#
#
#
# def main_menu():
#     while True:
#
#         num = input('1. Add flashcards\n2. Practice flashcards\n3. Exit\n')
#         if num == '1':
#             add_flash()
#         elif num == '2':
#             practice_flash()
#         elif num == '3':
#             print('\nBye!')
#             exit()
#         else:
#             print(f'{num} is not an option')
# main_menu()


import db_worker as dw


class Game:

    def __init__(self):
        self.main_menu = {
            '1': ('Add flashcards', self.input_card),
            '2': ('Practice flashcards', self.practice),
            '3': ('Exit', self.exit),
        }
        self.cards = dw.results
        self.boxes = 3
        self.cards_score = {}
        self.menu(self.main_menu, key_format='n')

    @staticmethod
    def menu(menu_items, key_format=None, **kwargs):
        def not_an_option(**kws):
            print(f'{kws["command"]} is not an option\n')

        def print_menu(menu):
            format_dict = {'s': lambda s: f'press "{s}" ', 'n': lambda n: f'{n}. ', None: lambda s: s}
            for key, value in menu.items():
                key = format_dict.get(key_format, format_dict[None])(key)
                print(f'{key}{value[0]}')
        try:
            while True:
                print_menu(menu_items)
                kwargs['command'] = input()
                print()
                menu_items.get(kwargs['command'], (None, not_an_option))[1](**kwargs)
        except StopIteration:
            pass

    def input_card(self, **kwargs):  # number 1 on main menu
        def input_true(text):
            while True:
                result = input(f'{text}:\n')
                if not result:
                    continue
                return result

        def add_card(**kws):
            dw.add_cards(input_true('Question'), input_true('Answer'))
            print()
        input_card_menu = {
            '1': ('Add a new flashcard', add_card),
            '2': ('Exit', self.exit),
        }
        self.menu(input_card_menu, key_format='n')

    def practice(self, **kwargs):  # number 2 on main menu
        def check_learning(**kws):
            self.menu(learning_menu, key_format='s', **kws)
            self.exit()

        def show_answer(**kws):
            if kws['command'] == 'y':
                print(f'Answer: {kws["card"].answer}')
            check_learning(**kws)
            self.exit()

        def true_answer(**kws):
            self.cards_score[kws['card']] += 1
            if self.cards_score[kws['card']] == 3:
                self.delete_card(**kws)
            self.exit()

        def false_answer(**kws):
            self.cards_score[kws['card']] = 0
            self.exit()

        practice_menu = {
            'y': ('to see the answer:', show_answer),
            'n': ('to skip:', show_answer),
            'u': ('to update:', self.update_card),
        }
        learning_menu = {
            'y': ('if your answer is correct:', true_answer),
            'n': ('if your answer is wrong:', false_answer),
        }

        if self.cards():
            for card in self.cards():
                self.cards_score[card] = self.cards_score.get(card, 0)
                print(f'Question: {card.question}')
                self.menu(practice_menu, key_format='s', card=card, **kwargs)
        else:
            print('There is no flashcard to practice!\n')

    @staticmethod  # number 3 on main menu
    def exit(**kwargs):
        raise StopIteration

    @staticmethod
    def delete_card(**kwargs):
        dw.delete_card(kwargs['card'].id)
        Game.exit()

    def update_card(self, **kwargs):
        def edit_card(card, **kws):
            def input_format(word, val):
                return f'current {word}: {val}\nplease write a new {word}:\n'
            dw.edit_card(card.id,
                         input(input_format('question', card.question)),
                         input(input_format('answer', card.answer))
                         )
            self.exit()

        update_menu = {
            'd': ('to delete the flashcard:', self.delete_card),
            'e': ('to edit the flashcard:', edit_card),
        }
        self.menu(update_menu, key_format='s', **kwargs)
        self.exit()


if __name__ == '__main__':
    Game()
    print('Bye!')