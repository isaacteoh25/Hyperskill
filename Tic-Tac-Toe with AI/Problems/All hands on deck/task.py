face_cards = {'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

count, total = 0, 0
while count < 6:
    card = input()
    try:
        card = int(card)
        total += card
    except ValueError:
        total += face_cards[card]
    count += 1

print(total / 6)

# deck = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
# card_list = [deck[input()] for _ in range(6)]
# print(sum(card_list) / 6)

# dic = {}
# z = 2
# x = '2 3 4 5 6 7 8 9 10 Jack Queen King Ace'
# for i in x.split():
#     dic[i] = z
#     z += 1
#
# s = 0
# inp = [input() for i in range(6)]
# for i in inp:
#     if i in dic:
#         s += dic[i]
# print(s / 6)

# dictionary = {"Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
#
# total = 0
# for _i in range(6):
#     entrada = str(input())
#     if entrada in dictionary:
#         total += dictionary.get(entrada)
#     else:
#         total += int(entrada)
# print(total / 6)

# MAX_INPUT = 6
# MIN_RANK = 2
# MAX_RANK = 10
# ranks = {
#     'Jack': 11,
#     'Queen': 12,
#     'King': 13,
#     'Ace': 14,
#     **{str(num): num for num in range(MIN_RANK, MAX_RANK + 1)}
# }
#
# result = 0
# for _ in range(MAX_INPUT):
#     a = input()
#     result += ranks.get(a)
# print(result / MAX_INPUT)

# cd = {'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
# fx = (lambda k: cd[k] if k in cd else int(k))
# print(sum([fx(input()) for _ in range(6)]) / 6)

# face_cards = {'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
# in_hand = 6
# hand = tuple(input() for x in range(in_hand))
# summ = 0
# for card in hand:
#     value = int(face_cards.get(card, card))
#     summ += value
# print(summ / len(hand))
