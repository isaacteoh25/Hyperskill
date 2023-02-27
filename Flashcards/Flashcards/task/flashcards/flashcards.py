# import random
# from io import StringIO
# import json
# import logging
# import sys
# import argparse
#
#
# class Flashcard:
#
#     def __init__(self):
#         """initiating the class using :
#         log=StringIO object to store a log file
#         flashcards = {} a dictionary to store the data"""
#
#         self.log = StringIO()
#         self.flashcards = {}
#
#     def get_log(self, func):
#         """prints the outputs both to console and to the log object"""
#         targets = logging.StreamHandler(sys.stdout), logging.StreamHandler(self.log)
#         logging.basicConfig(format='%(message)s', level=logging.INFO, handlers=targets)
#         logging.info(func)
#
#     def compare_answers(self, definition, answer):
#         """compares user's answer to the definition saved in the dictionary,
#         updates the 'mistakes' count if user's answer is wrong
#         returns an suitable response"""
#         term_list = list(self.flashcards.keys())
#         def_list = [self.flashcards[term]["word_def"] for term in term_list]
#
#         if answer != definition:
#             def_pos = def_list.index(definition)  # store the index for the definition
#             if answer in def_list:
#                 pos = def_list.index(answer)
#                 self.flashcards[term_list[def_pos]]["mistake"] += 1
#
#                 return f'Wrong. The right answer is "{definition}",\
#  but your definition is correct for "{term_list[pos]}".\n'
#             else:
#                 self.flashcards[term_list[def_pos]]["mistake"] += 1
#
#                 return f'Wrong. The right answer is "{definition}".\n'
#
#         return "Correct !\n"
#
#     def add_cards(self):
#         """adds user inputs data to the dictionary"""
#         message = f"The card:\n"
#         word_term = input(message)
#         print(message, word_term, file=self.log, flush=True)
#         definitions = [self.flashcards[card]["word_def"] for card in self.flashcards]
#         while word_term in self.flashcards.keys():
#             message = f'The card "{word_term}" already exists.\n'
#             word_term = input(message)
#             print(message, word_term, file=self.log, flush=True)
#         else:
#             message = f"The definition of the card:\n"
#             word_def = input(message)
#             print(message, word_def, file=self.log, flush=True)
#             while word_def in definitions:
#                 message = f'The definition "{word_def}" already exists.\n'
#                 word_def = input(message)
#                 print(message, word_def, file=self.log, flush=True)
#             else:
#                 self.flashcards[word_term] = {"word_def": word_def, "mistake": 0}
#                 return f'The pair ("{word_term}":"{word_def}") has been added.\n'
#
#     def remove_cards(self, card):
#         """removes a card from dictionary"""
#         try:
#             del self.flashcards[card]
#             return "The card has been removed.\n"
#         except KeyError:
#             return f'Can\'t remove "{card}": there is no such card.\n'
#
#     def import_from_file(self, file_name):
#         """imports data from an input file and updates data dictionary"""
#         try:
#             with open(file_name, "r+") as file:
#                 cards = json.load(file)
#             self.flashcards = self.flashcards or cards
#
#             return f"{len(cards)} cards have been loaded\n"
#         except FileNotFoundError:
#             return "File not found.\n"
#
#     def export_to_file(self, file_name):
#         """exports data from dictionary to a input file"""
#         with open(file_name, "w", encoding="utf-8") as file:
#             json.dump(self.flashcards, file)
#         return f"{len(self.flashcards)} cards have been saved.\n"
#
#     def ask(self):
#         """prompts user to enter the definition to a randomly chosen card
#         returns the compare_answers method as an answer"""
#         term_list = list(self.flashcards.keys())
#         word = random.choice(term_list)
#         message = f'Print the definition of "{word}":\n'
#         user_answer = input(message)
#         print(message, user_answer, file=self.log, flush=True)
#         return self.compare_answers(self.flashcards[word]["word_def"], user_answer)
#
#     def hardest_card(self):
#         """finds the cards with the biggest number of mistakes
#         returns a suitable message"""
#         term_list = list(self.flashcards.keys())
#         mistakes_list = [self.flashcards[card]["mistake"] for card in self.flashcards]
#         positions = [i for i, x in enumerate(mistakes_list) if x == max(mistakes_list) and x > 0]
#         if len(positions) == 1:
#             return f"The hardest card is {term_list[positions[0]]}. \
# You have {mistakes_list[positions[0]]} errors answering it.\n"
#         elif len(positions) == 0:
#             return f"There are no cards with errors.\n"
#         else:
#             hardest_list = [f'"{term_list[pos]}"' for pos in positions]
#             return f'The hardest cards are {"{}, " * len(hardest_list)}\n'.format(*hardest_list)
#
#     def reset_stats(self):
#         """reset all the mistakes counts"""
#         for card in self.flashcards:
#             self.flashcards[card]["mistake"] = 0
#         return f"Card statistics have been reset.\n"
#
#     def log_to_file(self, file_name):
#         """writes content of the log object to an input file"""
#         with open(file_name, "w") as file:
#             file.write(self.log.getvalue())
#         return f"The log has been saved.\n"
#
#     def exit_(self):
#         """prints a message on exit"""
#         return f"Bye Bye!\n"
#
#     def main(self):
#         """asks user for an input option and accesses the rest of the methods accordingly"""
#         while True:
#             menu = "Input the action (add, remove, import, export,\
#  ask, exit, log, hardest card, reset stats):\n"
#             user_choice = input(menu)
#             print(menu, user_choice, file=self.log, flush=True)
#             if user_choice == "exit":
#                 self.get_log(self.exit_())
#                 break
#             elif user_choice == "add":
#                 self.get_log(self.add_cards())
#             elif user_choice == "remove":
#                 message = input("Which card?\n")
#                 print(message, file=self.log, flush=True)
#                 self.get_log(self.remove_cards(message))
#             elif user_choice == "import":
#                 message = input("File name:\n")
#                 print(message, file=self.log, flush=True)
#                 self.get_log(self.import_from_file(message))
#             elif user_choice == "export":
#                 message = input("File name:\n")
#                 print(message, file=self.log, flush=True)
#                 self.get_log(self.export_to_file(message))
#             elif user_choice == "ask":
#                 n_times = input("How many times to ask?\n")
#                 print(n_times, file=self.log, flush=True)
#                 for _ in range(int(n_times)):
#                     self.get_log(self.ask())
#             elif user_choice == "log":
#                 message = input("File name:\n")
#                 print(message, file=self.log, flush=True)
#                 self.get_log(self.log_to_file(message))
#             elif user_choice == "hardest card":
#                 self.get_log(self.hardest_card())
#             elif user_choice == "reset stats":
#                 self.get_log(self.reset_stats())
#             else:
#                 self.get_log("No such option! Try again!")
#
#     def arg_parser(self):
#         """parser the arguments imputed by the user into the console"""
#         parser = argparse.ArgumentParser()
#         parser.add_argument("--import_from")
#         parser.add_argument("--export_to")
#         args = parser.parse_args()
#         if args.import_from and args.export_to:
#             self.get_log(self.import_from_file(args.import_from))
#             self.main()
#             self.get_log(self.export_to_file(args.export_to))
#         elif args.import_from:
#             self.get_log(self.import_from_file(args.import_from))
#             self.main()
#         elif args.export_to:
#             self.main()
#             self.get_log(self.export_to_file(args.export_to))
#         else:
#           self.main()
#
#
#
# # flashcards = {}
#
# # def main():
# #     print("Input the number of cards:")
# #     size = int(input())
# #     # a = input()
# #     for i in range(1, size + 1):
# #         print(f"The term for card #{i}:")
# #         term = input()
# #         definitions = [flashcards[card] for card in flashcards]
# #         while term in flashcards.keys():
# #             message = f'The term "{term}" already exists.\n'
# #             term = input(message)
# #         else:
# #             print(f"The definition for card #{i}:")
# #             definition = input()
# #             flashcards[term] = definition
# #             while definition in definitions:
# #                 message = f'The definition "{definition}" already exists.\n'
# #                 definition = input(message)
# #                 flashcards[term] = definition
# #         # add_cards(i)
# #     for r in flashcards:
# #         print(f"Print the definition of \"{r}\":")
# #         c = input()
# #         if flashcards[r] == c :
# #             print("Correct!")
# #         else:
# #             print(wrong_ans(c, r))
# #             # print(compare_answers(flashcards[c], c))
# #             # print(f"Wrong. The right answer is \"{flashcards[r]}\".")
# #
# #
# # def wrong_ans(c, r):
# #     for key, val in flashcards.items():
# #         if c == val:
# #             return (f"""Wrong. The right answer is "{flashcards[r]}", but your definition is correct for "{key}".""")
# #     return f"Wrong. The right answer is \"{flashcards[r]}\"."
#
#
# flashcard = Flashcard()
# if __name__ == "__main__":
#     flashcard.arg_parser()
#     # main()
#
#
#
# Write your code here
import json
import os.path
from io import StringIO
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--import_from')
parser.add_argument('--export_to')
args = parser.parse_args()


class FlashCard:
    list_of_flashcards = []
    mem_buffer = StringIO()

    def __init__(self, in_term, in_definition, in_mistakes=0):
        self.term = in_term
        self.definition = in_definition
        self.mistakes = in_mistakes

    def __str__(self):
        return f'Card:\t{self.term}\nDefinition:\t{self.definition}\nMistakes:\t{self.mistakes}'

    def check_answer(self, in_str):
        if in_str == self.definition:
            FlashCard.print_and_log('Correct!')
        else:
            self.mistakes += 1
            correct_term = FlashCard.search_correct_term(in_str)
            if correct_term:
                FlashCard.print_and_log(
                    f'Wrong. The right answer is "{self.definition}", but your definition is correct for "{correct_term}.')
            else:
                FlashCard.print_and_log(f'Wrong. The right answer is "{self.definition}".')

    @staticmethod
    def print_and_log(string):
        if string is not None:
            FlashCard.mem_buffer.read()
            FlashCard.mem_buffer.write(string + '\n')
        print(string)

    @staticmethod
    def input_and_log(string):
        FlashCard.print_and_log(string)
        in_input = input()
        FlashCard.mem_buffer.read()
        FlashCard.mem_buffer.write(in_input + '\n')
        return in_input

    @staticmethod
    def save_log(file_name):
        with open(file_name, 'w', encoding='utf-8') as log:
            for line in FlashCard.mem_buffer.getvalue():
                log.write(line)
        print('The log has been saved.')

    @staticmethod
    def search_correct_term(in_definition):
        for flashcard in FlashCard.list_of_flashcards:
            if flashcard.definition == in_definition:
                return flashcard.term
        return None

    @staticmethod
    def search(type_c, in_str):
        for flashcard in FlashCard.list_of_flashcards:
            if type_c == 't':
                if flashcard.term == in_str:
                    return flashcard.term
            elif type_c == 'd':
                if flashcard.definition == in_str:
                    return flashcard
        return None

    @staticmethod
    def search_hardest():
        higher = 0
        for flashcard in FlashCard.list_of_flashcards:
            if flashcard.mistakes > higher:
                higher = flashcard.mistakes
        if higher:
            hardest_card = [flashcard for flashcard in FlashCard.list_of_flashcards if flashcard.mistakes == higher]
            if len(hardest_card) > 1:
                hardest_list = [flashcard.term for flashcard in hardest_card]
                FlashCard.print_and_log(f'''The hardest cards are "{'", "'.join(hardest_list)}".''')
            else:
                FlashCard.print_and_log(
                    f'The hardest card is "{hardest_card[0].term}". You have {hardest_card[0].mistakes} errors answering it.')
        else:
            FlashCard.print_and_log('There are no cards with errors.')

    @staticmethod
    def reset_stats():
        for card in FlashCard.list_of_flashcards:
            card.mistakes = 0
        FlashCard.print_and_log('Card statistics have been reset.')

    @staticmethod
    def add():
        # number_of_flashcards = int(input('Input the number of cards:\n'))
        # for i in range(number_of_flashcards):
        card = FlashCard.input_and_log(f'The term for card:')
        while FlashCard.search('t', card):
            card = input(f'The term "{card}" already exists. Try again:')
        definition = FlashCard.input_and_log(f'The definition for card:')
        while FlashCard.search('d', definition):
            definition = FlashCard.input_and_log(f'The definition "{definition}" already exists. Try again:')
        flashcard = FlashCard(card, definition)
        FlashCard.list_of_flashcards.append(flashcard)
        FlashCard.print_and_log(FlashCard.save(flashcard, 'flashcards.json'))

    @staticmethod
    def remove(term):
        if FlashCard.search('t', term):
            for flashcard in FlashCard.list_of_flashcards:
                if flashcard.term == term:
                    FlashCard.list_of_flashcards.remove(flashcard)
                    FlashCard.print_and_log('The card has been removed.')
                    break
        else:
            FlashCard.print_and_log(f'Can\'t remove "{term}": there is no such card.')

    @staticmethod
    def load(file_name):
        if os.path.isfile(file_name):
            n_cards_loaded = 0
            with open(file_name, 'r') as file:
                data = json.load(file)
                for k, v in data['flashcards'].items():
                    if FlashCard.search('t', k):
                        FlashCard.search.definition = v['def']
                        FlashCard.search.mistakes = v['mistake_number']
                        n_cards_loaded += 1
                    else:
                        card = FlashCard(k, v['def'], v['mistake_number'])
                        FlashCard.list_of_flashcards.append(card)
                        n_cards_loaded += 1
            FlashCard.print_and_log(f'{n_cards_loaded} cards have been loaded')
        else:
            FlashCard.print_and_log('File not found.')

    @staticmethod
    def write_json(data, filename):
        with open(filename, 'w+') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def save(flashcard, file_name):
        data = {flashcard.term: {'def': flashcard.definition, 'mistake_number': flashcard.mistakes}}
        if not os.path.isfile(file_name):
            first_data = {'flashcards': data}
            FlashCard.write_json(first_data, file_name)
        else:
            with open(file_name, 'r') as json_file:
                data_from_file = json.load(json_file)
                temp = data_from_file.get('flashcards')
                temp.update(data)
            FlashCard.write_json(data_from_file, filename=file_name)
        return f'The pair ("{flashcard.term}":"{flashcard.definition}") has been added.'

    @staticmethod
    def export(file_name):
        saved_cards = 0
        for card in FlashCard.list_of_flashcards:
            FlashCard.save(card, file_name)
            saved_cards += 1
        FlashCard.print_and_log(f'{saved_cards} cards have been saved.')

    @staticmethod
    def ask():
        times = int(FlashCard.input_and_log('How many times to ask?'))
        i = 0
        index = 0
        while i < times:
            if index >= len(FlashCard.list_of_flashcards):
                index = 0
            FlashCard.print_and_log(f'Print the definition of "{FlashCard.list_of_flashcards[index].term}":')
            FlashCard.list_of_flashcards[index].check_answer(FlashCard.input_and_log(''))
            i += 1
            index += 1

    @staticmethod
    def menu():
        if args.import_from:
            FlashCard.load(args.import_from)
        action = ''
        while action != 'exit':
            action = FlashCard.input_and_log(
                'Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):')
            if action == 'add':
                FlashCard.add()
            if action == 'remove':
                FlashCard.remove(FlashCard.input_and_log('Which card?'))
            if action == 'import':
                if args.import_from:
                    FlashCard.load(args.import_from)
                else:
                    FlashCard.load(FlashCard.input_and_log('File name:'))
            if action == 'export':
                if args.export_to:
                    FlashCard.export(args.export_to)
                else:
                    FlashCard.export(FlashCard.input_and_log('File name:'))
            if action == 'ask':
                FlashCard.ask()
            if action == 'hardest card':
                FlashCard.search_hardest()
            if action == 'reset stats':
                FlashCard.reset_stats()
            if action == 'log':
                FlashCard.save_log(FlashCard.input_and_log('File name:'))
            if action == 'buffer':
                print(FlashCard.mem_buffer.getvalue())
            if action == 'exit':
                if args.export_to:
                    FlashCard.export(args.export_to)
        FlashCard.print_and_log('Bye bye!')


FlashCard.menu()