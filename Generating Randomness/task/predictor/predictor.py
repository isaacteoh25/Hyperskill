import itertools
import random

# The limit for the extended ASCII Character set
import re

import numpy as np

random_string = ''
bit = ['0', '1']

cnt = 0
maxl = 100
print("Please give AI some data to learn...")
print("The current data length is 0, 100 symbols left")
print("Print a random string containing 0 or 1:\n")
while len(random_string) < maxl:

    ch = input()
    for c in ch:
        if c in bit:
            random_string += c
            cnt += 1
            # if cnt == 20:
            #     break
    print(f"Current data length is {cnt}, { maxl - cnt} symbols left")

print("Final data string:")
print(random_string)
# print(random_string, len(random_string))

print("""\nYou have $1000. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!
""")
x = [0,1]
l = itertools.product(x, repeat=3)
lst = []
for p in l:
    s = ""
    for i in p:
        s+=str(i)
    lst.append(s)
for comb in lst:
    cnt1 = len(re.findall(f'(?={comb}0)', random_string))
    cnt2 = len(re.findall(f'(?={comb}1)', random_string))
    # print(f'{comb}: {cnt1},{cnt2}')

# x = [0,1]
# l = itertools.product(x, repeat=3)
# lst = []
# for p in l:
#     s = ""
#     for i in p:
#         s+=str(i)
#     lst.append(s)
# for comb in lst:
#     cnt1 = len(re.findall(f'(?={comb}0)', random_string))
#     cnt2 = len(re.findall(f'(?={comb}1)', random_string))
#     print(f'{comb}: {cnt1},{cnt2}')


def remember_data(data, count_dict):
    for i in range(len(data) - COMBO_LENGTH):
        comb = data[i:i + COMBO_LENGTH]
        next_input = int(data[i + COMBO_LENGTH])
        count_dict[comb][next_input] += 1

    return count_dict


def make_prediction(data, count_dict):
    pred = str()
    for i in range(COMBO_LENGTH):
        res = str(np.random.choice([0, 1]))
        pred += res

    for i in range(len(data) - COMBO_LENGTH):
        comb = data[i:i + COMBO_LENGTH]
        try:
            if count_dict[comb][0] > count_dict[comb][1]:
                probas = [1, 0]
            elif count_dict[comb][0] < count_dict[comb][1]:
                probas = [0, 1]
            else:
                probas = [0.5, 0.5]



        except Exception:
            probas = [0.5, 0.5]

        res = str(np.random.choice([0, 1], p=probas))
        pred += res

    return pred

COMBO_LENGTH = 3

def estimate_prediction_accuracy(pred, data):
    pr = [bool(int(elem)) for elem in pred]
    gt = [bool(int(elem)) for elem in data]
    pred_correct = ~np.bitwise_xor(pr, gt)
    return sum(pred_correct.astype(int))

# for _ in range(maxl):
#     random_integer = random.randint(0, maxl)
#     # Keep appending random characters using chr(x)
#     random_string += (str(random_integer))
keys = []
for i in range(2**COMBO_LENGTH):
    keys.append(str((bin(i)[2:].zfill(3))))

values = [[0, 0] for _ in range(2**COMBO_LENGTH)]
count_dict = dict(zip(keys, values))

cash = 1000
while True:
    print("Print a random string containing 0 or 1")
    inp = input()
    if inp =="some_irrelevant_symbols_in_the_game":
        inp = input()
    if inp == 'enough':
        print("Game over!")
        break
    # inp = '1010101101010101010011100101001010100101010000101000101010000100101011010001001000101011101000101010010100101'
    count_dict = remember_data(inp, count_dict)

    # appr_pred_set = set()
    # for i in range(1000):
    #     pred = make_prediction(inp, count_dict)
    #     appr_pred_set = appr_pred_set | set([pred[COMBO_LENGTH:]])
    pred = make_prediction(inp, count_dict)

    predictor = pred[COMBO_LENGTH:]
    appr_pred_output_dict = {}
    # for appr_pred in appr_pred_set:
    correct_guesses = estimate_prediction_accuracy(predictor, inp[COMBO_LENGTH:])
    ideal_output = 'Computer guessed right {} out of {} symbols ({:03.2f} %)'.format(correct_guesses,
                                                                                        len(inp)-COMBO_LENGTH,
                                                                                        100 * correct_guesses / (len(inp)-COMBO_LENGTH))

    print("prediction:")
    print(pred + "\n")
    print(ideal_output)
    cash = cash - correct_guesses + (len(inp) - COMBO_LENGTH - correct_guesses)
    print(f"Your capital is now ${cash}")
    appr_pred_output_dict[predictor] = ideal_output


import itertools
import re
print('''Please give AI some data to learn...
The current data length is 0, 100 symbols left
Print a random string containing 0 or 1''')
final = ""
n = 100
while len(final)<n:
    s = input()
    for char in s:
        if char == "0" or char == "1":
            final += char
    if len(final)<n:
        print(f'Current data length is {len(final)}, {n - len(final)} symbols left')
print(f"Final data string:\n{final}")
x = [0,1]
l = itertools.product(x, repeat=3)
lst = []
for p in l:
    s = ""
    for i in p:
        s+=str(i)
    lst.append(s)
my_dic_0 = {}
my_dic_1 = {}
for comb in lst:
    cnt1 = len(re.findall(f'(?={comb}0)', final))
    cnt2 = len(re.findall(f'(?={comb}1)', final))
    my_dic_0[comb] = cnt1
    my_dic_1[comb] = cnt2
cnt_0 = 0
cnt_1 = 0
for key in my_dic_0:
    cnt_0 += my_dic_0[key]
for key in my_dic_1:
    cnt_1 += my_dic_1[key]

capital = 1000
print('''You have $1000. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!\n''')
print('Print a random string containing 0 or 1:')
user_input = input()
while user_input != 'enough':
    inp = ''
    for char in user_input:
        if char == "0" or char == "1":
            inp += char
    if len(inp) != 0:
        inp = list(inp)
        out = ''
        if cnt_0 > cnt_1:
            out += '000'
        else:
            out += '111'
        for i in range(0, len(inp)-3):
            chunk = inp[i:i+3]
            chunk = "".join(chunk)
            if int(my_dic_0[chunk]) > int(my_dic_1[chunk]):
                out += '0'
            else:
                out += '1'
        print(f'prediction:\n{out}')
        correct = 0
        wrong = 0
        for idx in range(len(list(out)))[3:]:
            if inp[idx] == out[idx]:
                correct += 1
            else:
                wrong += 1
        all = correct + wrong
        print(f'Computer guessed right {correct} out of {all} symbols ({round(100 * correct / all, 2)} %)')
        capital = capital - correct + wrong
        print(f'Your capital is now ${capital}')
    print('Print a random string containing 0 or 1:')
    user_input = input()
print('Game over!')

