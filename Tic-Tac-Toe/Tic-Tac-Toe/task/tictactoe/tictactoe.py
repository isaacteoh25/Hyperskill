# valid_input = ('X','O','_')
user_input = "_________"   #input("Enter cells:")
ulist = user_input.replace('_', " ")
input_list = list(ulist)  # turns the string input into

def validateInput(cord2,tup):
    global input_list
    # if type(input_list[0]) is not int:
    #     print("You should enter numbers!")
    #     return True
    if len(cord2) != 2:
        print("Input must be two numbers in format row,col e.g.  1,2 ")
        return True
    # input is a number between 1 and 3 (inclusive)
    if (1 <= int(cord2[0]) <= 3) and (1 <= int(cord2[1]) <= 3):
        count = 0
        for item in tup:
            if (item[0] == cord2[0]) and (item[1] == cord2[1]):

                if input_list[count] == 'O' or input_list[count] == 'X':
                    print("This cell is occupied! Choose another one!")
                    return True
                o_num = 0
                x_num = 0
                if input_list.count('X') > input_list.count('O'):
                    input_list[count] = 'O'
                else:
                    input_list[count] = 'X'
                # if o_num<=x_num:
                #     input_list[count] = 'X'
                # else:
                #     input_list[count] = 'O'
                for i in range(0, 9):
                    if input_list[i] == 'X':
                        x_num += 1
                    if input_list[i] == 'O':
                        o_num += 1
                print_list(input_list)
                # isWinner()

                if isWinner(input_list, 'X') and not isWinner(input_list, 'O'):
                    print("X wins")
                    return False
                elif isWinner(input_list, 'O') and not isWinner(input_list, 'X'):
                    print("O wins")
                    return False
                elif (isWinner(input_list, 'X') and isWinner(input_list, 'O') or not isWinner(input_list, 'X') and not isWinner(
                        input_list, 'O') and abs(x_num - o_num) >= 2) \
                        or (x_num + o_num) == 9:
                    print("Draw")
                    return False
                return True
            count += 1
    else:
        print("Coordinates should be from 1 to 3")
        return True


# def isWinner(bo, le):
#     if bo == le[0] == le[1] == le[2]:
#         return True
#     if bo==le[3] == le[4] == le[5]:
#         return True
#     if bo==le[6] == le[7] == le[8]:
#         return True
#     if bo==le[0] == le[3] == le[6]:
#         return True
#     if bo==le[1] == le[4] == le[7]:
#         return True
#     if bo==le[2] == le[5] == le[8]:
#         return True
#     if bo==le[0] == le[4] == le[8]:
#         return True
#     if bo==le[2] == le[4] == le[6]:
#         return True
#     else:
#         return False
def isWinner(bo, le):
    return ((bo[0] == le and bo[1] == le and bo[2] == le) or  # across the top

            (bo[3] == le and bo[4] == le and bo[5] == le) or  # across the middle

            (bo[6] == le and bo[7] == le and bo[8] == le) or  # across the bottom

            (bo[0] == le and bo[3] == le and bo[6] == le) or  # down the left side

            (bo[1] == le and bo[4] == le and bo[7] == le) or  # down the middle

            (bo[2] == le and bo[5] == le and bo[8] == le) or  # down the right side

            (bo[0] == le and bo[4] == le and bo[8] == le) or  # diagonal

            (bo[2] == le and bo[4] == le and bo[6] == le))  # diagonal



def print_list(input_list):
    print("---------")
    print("|", *list(input_list)[0:3], "|", sep=' ')  # this first prints the list indexes, then sperates them by spaces
    print("|", *list(input_list)[3:6], "|", sep=' ')
    print("|", *list(input_list)[6:9], "|", sep=' ')
    print("---------")


print_list(input_list)

looping = True
while looping:

    cord = str(input("Enter the coordinates:"))
    cord2 = tuple(map(int, cord.split(' ')))

    tup = [(1, 3),(2, 3),(3, 3),
           (1, 2),(2, 2),(3, 2),
            (1, 1),(2, 1),(3, 1)]

    looping= validateInput(cord2,tup)

    # if isWinner(input_list, 'X') and isWinner(input_list, 'O') or not isWinner(input_list, 'X') and not isWinner(input_list, 'O') and abs(
    #         x_num - o_num) >= 2:
        # print("Impossible")
        # looping = False
    # if isWinner(input_list, 'X') and not isWinner(input_list, 'O'):
    #     print("X wins")
    #     # looping=False
    # elif isWinner(input_list, 'O') and not isWinner(input_list, 'X'):
    #     print("O wins")
        # looping = False
    # elif "_" not in input:
    #     print("Draw")
    #     looping = False
        # XO_OOX_X_
    # elif not isWinner(input_list, 'X') or not isWinner(input_list, 'O'):
    #     if "_" in input:
    #         print("Game not finished")
    #         looping = False
   # isWinner(bo,le)

    

  




    

  


