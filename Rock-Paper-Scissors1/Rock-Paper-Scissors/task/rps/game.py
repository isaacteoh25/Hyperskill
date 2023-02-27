# import collections
# import random
#
# # decider = {"scissors": "rock", 'rock': 'paper', 'paper': 'scissors'
# #            }
# # game_options = ['scissors', 'rock', 'paper']
#
# def game_result(user_choice, computer_choice, dic):
#
#     # for i in game_options:
#     #         dictionary[i] = list(game_options[l])
#     # index = game_options.index(computer_choice)
#     if user_choice == computer_choice:
#         result = (f'There is a draw {user_choice}', 50)
#     elif computer_choice in dic[user_choice]:
#         result = f'Sorry but computer chose {computer_choice}', 0
#     elif computer_choice not in dic[user_choice]:
#         result = f'Well done. Computer chose {computer_choice} and failed', 100
#
#     return result
#
#
# def get_scores():
#     ratings = open('rating.txt').readlines()
#     scores = {}
#     for rating in ratings:
#         player, score = rating.strip().split(' ')
#         scores[player] = score
#     return scores
#
#
# def save_scores(scores):
#     with open('rating.txt', 'w') as f:
#         for name, score in scores.items():
#             f.write(f'{name} {score}\n')
#
# list1 = []
# def main():
#     player_name = input('Enter your name: > ')
#     print(f'Hello {player_name}')
#     # print("rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire\nOkay, let's start")
#     list_1 = input()
#     list_1 = list_1.split(',')
#     if list_1[0] == '':
#         list_1 = ['rock','paper','scissors']
#     print("Okay, let's start")
#     dic = {}
#     game_list= list_1
#     # length = len(list_1)
#     for a in range(len(list_1)):
#         list_1 = collections.deque(list_1)
#         shifted_list = list(list_1)
#         dic[game_list[a]] =shifted_list[1:len(list_1)//2 + 1]
#         list_1.rotate(-1)
#
#         # dic[game_list[a]] = list_1[1: len(list_1) // 2 + 1]
#         # list_1 = (list_1[len(list_1) - 1:len(list_1)]
#         #           + list_1[0:len(list_1) - 1])
#
#     all_scores = get_scores()
#     player_score = all_scores.get(player_name, 0)
#
#     while True:
#         user_choice = input().lower()
#         if user_choice == '!exit':
#             all_scores[player_name] = player_score
#             save_scores(all_scores)
#             print('Bye!')
#             break
#         elif user_choice == '!rating':
#             print(player_score)
#         elif user_choice in list_1:
#             computer_choice = random.choice(list_1)
#             message, score = game_result(user_choice, computer_choice, dic)
#             print(message)
#             player_score += int(score)
#         else:
#             print('Invalid Input')
#
#
# main()

# import random
# rating = 0
#
# name = input("Enter your name: ")
# print(f"Hello, {name}")
# plik = open("rating.txt", "r")
# names = [x.split(" ") for x in plik.read().split("\n")]
# for x in names:
#     if x[0] == name:
#         rating = int(x[1])
# plik.close()
# elements = input().split(",")
# if elements == ['']:
#     elements = ["rock", "paper", "scissors"]
# print("Okay, let's start")
#
# while True:
#     player = input()
#     if player == "!exit":
#         break
#     elif player == "!rating":
#         print(f"Your rating: {rating}")
#     else:
#         if player in elements:
#             ile = int((len(elements) - 1) / 2)
#             gdzie = elements.index(player)
#             wins = [elements[x % len(elements)] for x in range(gdzie + 1, gdzie + ile + 1)]
#             random.seed()
#             computer = random.choice(elements)
#             if computer == player:
#                 print(f"There is a draw ({computer})")
#                 rating += 50
#             elif computer in wins:
#                 print(f"Sorry, but computer chose {computer}")
#             else:
#                 print(f" Well done. Computer chose {computer} and failed")
#                 rating += 100
#         else:
#             print("Invalid input")
# print("Bye!")

# # Write your code here
# import os
# import re
# from random import choice
#
# global name
# def appendFile(file, name):
#     # for filename in os.listdir(os.getcwd()):
#     #     # if the filename ends with m.txt
#     #     if filename[-5:] == file:
#             # open the file
#     with open(file, encoding='utf-8') as fp:
#         lines = fp.read().splitlines()
#     with open(file, "a", encoding='utf-8') as fp:
#         for line in lines:
#             d = line.split()
#             if name == d[0]:
#                 break
#         else:
#             fp.write("\n" +name + " " + str(0))
#     fp.close()
#
#
# def ModifyFile(file, name, point):
#     with open(file, encoding='utf-8') as fp:
#         lines = fp.read().splitlines()
#     with open(file, "w", encoding='utf-8') as fp:
#         for line in lines:
#             d = line.split()
#             if name == d[0]:
#                 print(d[0] + " " + str(int(d[1]) + point), file=fp)
#             else:
#                 print(line, file=fp)
#     fp.close()
# def start():
#     name = input("Enter your name:")
#     print(f"Hello, {name}")
#     file = "rating.txt"
#     appendFile(file, name)
#     while True:
#         player = input()
#
#         computer = ["rock", "scissors", "paper"]
#         if player == "scissors":
#             option = choice(computer)
#             if option == "rock":
#                 print("Sorry, but computer chose {0}".format(computer[0]))
#             elif option == "scissors":
#                 print("There is a draw ({0})".format(computer[1]))
#                 # a = open('rating.txt', 'r')
#                 ModifyFile(file, name, 50)
#
#             else:
#                 print(f"Well done. Computer chose {option} and failed")
#                 ModifyFile(file, name, 100)
#         elif player == "paper":
#             option = choice(computer)
#             if option == "scissors":
#                 print("Sorry, but computer chose {0}".format(computer[1]))
#             elif option == "paper":
#                 print("There is a draw ({0})".format(computer[2]))
#                 ModifyFile(file, name, 50)
#             else:
#                 print(f"Well done. Computer chose {option} and failed")
#                 ModifyFile(file, name, 100)
#         elif player == "rock":
#             option = choice(computer)
#             if option == "paper":
#                 print("Sorry, but computer chose {0}".format(computer[2]))
#             elif option == "rock":
#                 print("There is a draw ({0})".format(computer[0]))
#                 ModifyFile(file, name, 50)
#             else:
#                 print(f"Well done. Computer chose {option} and failed")
#                 ModifyFile(file, name, 100)
#         elif player == "!rating":
#             rating = printRating(file, name)
#             print(f"Your rating: {rating}")
#         elif player == "!exit":
#             print("Bye!")
#             break
#         else:
#             print("Invalid input")
#
#
# def printRating(file, name):
#     with open(file, encoding='utf-8') as fp:
#         lines = fp.read().splitlines()
#         for line in lines:
#             d = line.split()
#             if d[0] == name:
#                 rating = d[1]
#     fp.close()
#     return rating
#
#
# start()


import random
with open('rating.txt', 'r+') as file:
    scoreboard = dict(x.split() for x in file.read().split('\n'))
rating = 0
name = input("Enter your name: ")
print(f"Hello, {name}")
rules = input().split(',')
print("Okay, let's start")
conditions = dict()
if len(rules) <= 2 or len(rules) % 2 == 0:
    #print(len(rules))
    rules = ['rock', 'paper', 'scissors']
    conditions.update({
      'rock':{'rock':'draw', 'paper':False, 'scissors':True},
      'paper':{'rock':True, 'paper':'draw', 'scissors':False},
      'scissors':{'rock':False, 'paper':True, 'scissors':'draw'}
      })
else:
    for rule in rules:
      conditions.update({rule:{}})
      options = rules[rules.index(rule) + 1:] + rules[:rules.index(rule)]
      for option in options[:int(len(options) / 2)]:
          conditions[rule].update({option:False})
      conditions[rule].update({rule:'draw'})
      for option in options[int(len(options) / 2):]:
          conditions[rule].update({option:True})
if name in scoreboard.keys():
    rating = int(scoreboard[name])
while True:
    user_move = input()
    computer_move = random.choice(rules)
    #print(computer_move)
    try:
        if conditions.get(user_move) == None:
            raise Exception
        elif user_move == computer_move:
            print(f"There is a draw ({computer_move})")
            rating += 50
        elif conditions.get(user_move).get(computer_move):
            print(f"Well done. Computer chose {computer_move} and failed")
            rating += 100
        elif not conditions.get(user_move).get(computer_move):
            print(f"Sorry, but computer chose {computer_move}")
    except:
        if user_move == "!exit":
            print("Bye!")
            break
        elif user_move == "!rating":
            print(f"Your rating: {rating}")
        else:
            print("Invalid input")