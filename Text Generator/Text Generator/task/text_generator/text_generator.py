# # import nltk
# # import re
# # from nltk.corpus import words
# #
# #
# # def main_func():
# #     running = True
# #
# #     while running:
# #         user_input = input()
# #         if user_input == "exit":
# #             running = False
# #         elif ".txt" in user_input:
# #             with open(user_input, "r", encoding="utf-8") as file:
# #                 # data = file.read().split()
# #                 # data = [(x, i.split()[j + 1]) for i in file.read()
# #                 #  for j, x in enumerate(i.split()) if j < len(i.split()) - 1]
# #                 # print(data)
# #                 nltk_tokens = file.read().split()# nltk.split(file.read())
# #                 # print(f"Number of bigrams: {len(list(nltk.bigrams(nltk_tokens)))}")
# #                 # print("Corpus statistics")
# #                 # print(f"All tokens: {len(data)}")
# #                 # print(f"Unique tokens: {len(set(data))}")
# #             # print(bigram_counts(list(nltk.bigrams(nltk_tokens))))
# #         else:
# #             try:
# #                 from collections import defaultdict
# #
# #                 freq_defaultdict = defaultdict(int)
# #                 count = 0
# #                 word = user_input
# #
# #                 print(f"Head: {word}")
# #                 for i in list(nltk.bigrams(nltk_tokens)):
# #                     # if word.__contains__(i[0]):
# #                     if word in i[0]: #word in i[0]:
# #                         freq_defaultdict[i[1]] += 1
# #                 for k, i in freq_defaultdict.items():
# #                     print(f"Tail: {k} Count: {i}")
# #                 # print(f"Head: {list(nltk.bigrams(nltk_tokens))[a][0]} Tail: {list(nltk.bigrams(nltk_tokens))[a][1]}")
# #             except ValueError:
# #                 print("Type Error. Please input an integer.")
# #             except IndexError:
# #                 # print("Index Error. Please input an integer that is in the range of the corpus.")
# #                 print("Index Error. Please input a value that is not greater than the number of all bigrams.")
# #
# # if __name__ == '__main__':
# #     main_func()
#
# # import os
# # import random
# #
# # import nltk
# #
# # f_name = input()
# # # f_name = 'corpus.txt'
# # path = os.getcwd()
# # with open(os.path.join(path, f_name), 'r', encoding='utf-8') as file:
# #     corpus = file.read()
# #
# # tokens = corpus.split()
# # bigrams = list(nltk.bigrams(tokens))
# #
# # head_tail = {}
# # for head, tail in bigrams:
# #     head_tail.setdefault(head, []).append(tail)
#
# # while (head := input()) != 'exit':
# # head = input()
# # b = []
# # for r in range(10):
# #     a =[]
# #     a.append()
# #     for i in range(8):
# #         head = random.choice(tokens)
# #         a.append(head)
# #     sen = ' '.join(a)
# #     b.append(sen)
# # word = "\n".join(b)
# # print(word)
# import random
# import nltk
#
#
# # Write your code here
# def main_func():
#     with open(input(), "r", encoding="utf-8") as file:
#         data = nltk.sent_tokenize(file.read())
#         count = 0
#         pun = [".", "?", "!"]
#
#         while count < 10:
#             random_word = random.choice(data)
#             split_word = random_word.split()
#             if (len(split_word) > 5) and (split_word[0][-1] not in pun) and (split_word[0].istitle()) and (
#                     "\n" not in random_word):
#                 count += 1
#                 print(random_word)
#
#
# if __name__ == '__main__':
#     main_func()
#
#
# import re
# from collections import defaultdict, Counter
# from random import choice, choices
# from nltk.tokenize import regexp_tokenize
#
# file_name = input()
# corpus = open(file_name, "r", encoding="utf-8")
#
# tokens = regexp_tokenize(corpus.read(), r"\S+")
# bigrams = [(tokens[i], tokens[i + 1]) for i in range(len(tokens) - 1)]
#
# tails = defaultdict(list)
# for h, t in bigrams:
#     tails[h].append(t)
# for h in tails:
#     tails[h] = Counter(tails[h]).most_common()
#
#
# def next_word(head):
#     global tails
#     word_tails = [k for k, v in tails[head]]
#     weights = [v for k, v in tails[head]]
#     return choices(word_tails, weights)[0]
#
#
# def generate_text(init, length=None):
#     head = init
#     text_list = [head]
#     while len(text_list) < 5 or not re.match(r'.*[.?!]$', text_list[-1]):
#         tail = next_word(head)
#         text_list.append(tail)
#         head = tail
#     return ' '.join(text_list)
#
#
# for _ in range(10):
#     first_word = 'a.'
#     while not re.match(r'^[A-Z].*[^!.?]$', first_word):
#         first_word = choice(list(tails.keys()))
#     print(generate_text(first_word))
# # try:
# #     tails = nltk.Counter(head_tail[head])
# #     print(f'Head: {head}')
# #     for tail, count in tails.items():
# #         # print(f'Tail: {str(tail).ljust(10)}Count: {int(count)}')
# #         print(f"Tail: {tail} Count: {int(count)}")
# #     # print('\n')
# # except ValueError:
# #     print("Type Error. Please input an integer.")
# # except IndexError:
# #     # print("Index Error. Please input an integer that is in the range of the corpus.")
# #     print("Index Error. Please input a value that is not greater than the number of all bigrams.")
#
#     # except KeyError:
#     #     print('Key Error. The requested word is not in the model. Please input another word.\n')


from random import choice, choices
from nltk.tokenize import WhitespaceTokenizer
from collections import defaultdict, Counter

"""This project uses some basic nltk features as well as other libraries to
generate preudo sentences using the idea of markow chains."""


class TextGenerator:

    def __init__(self):
        self.path = input()
        self.tokens = self.tokens()
        self.ngrams = self.ngrams()

    def read_file(self):
        """method is used to read the corpus file that will be used
        to generate the sentences"""

        with open(self.path, encoding="utf-8") as file:
            text = file.read()
        return text

    def tokens(self):
        """method is used to parse the text file and to return
        a list of all tokens"""
        text = self.read_file()
        tk = WhitespaceTokenizer()
        return tk.tokenize(text)

    def ngrams(self):
        """method returns a dict using every 2 words as key and the value is a counter dict of every word
         that is a possible folower of the first 2 words(like nltk.FreqDist)"""
        ngrams = defaultdict(Counter)
        for i in range(len(self.tokens) - 2):
            ngrams[" ".join(self.tokens[i:i + 2])].update((self.tokens[i + 2],))
        return ngrams

    def find_start(self):
        """method is used to find the first words of the sentence"""
        starts = [pair for pair in list(self.ngrams) if pair.split()[0][0].isupper() and pair.split()[0][-1] not in "!?."]
        return choice(starts).split()

    def make_sentence(self, n=5):
        """main method of the script. It randomly chooses the next words in
        sentence accordingly to their weight in the original text and returns the new sentence"""
        result = []
        while True:
            if len(result) == 0:
                result = self.find_start()
            w1 = " ".join(result[-2:])
            w2 = choices(list(self.ngrams[w1].keys()), list(self.ngrams[w1].values()))
            result.append(*w2)

            if w2[0][-1] in ".!?":
                if len(result) < n:
                    result = []
                    continue
                return " ".join(result)


if __name__ == "__main__":
    text_gen = TextGenerator()
    for _ in range(10):
        print(text_gen.make_sentence())