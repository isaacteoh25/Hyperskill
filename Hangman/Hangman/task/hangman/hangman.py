# Write your code here
from random import choice
computer = ['python', 'java', 'kotlin', 'javascript']
current_word = choice(computer)
guessed_word = list("-" * len(current_word))
attempts_number = 8
abc_list = "abcdefghijklmnopqrstuvwxyz"
user_letters = []
user_decision = ''
print("""H A N G M A N""")
while user_decision != 'play':
    user_decision = input('Type "play" to play the game, "exit" to quit: ')
while attempts_number != 0:

    print()
    print(''.join(guessed_word))
    current_letter = input("Input a letter: ")

    if current_letter in abc_list and len(current_letter) == 1:
        if current_letter in current_word or current_letter in user_letters:
            if current_letter not in guessed_word and current_letter not in user_letters:
                for i in range(len(current_word)):
                    if current_word[i] == current_letter:
                        guessed_word[i] = current_letter
                if current_word == "".join(guessed_word):
                    print("You guessed the word "+ current_word +"!\nYou survived!")
                    break
                # if current_word == "".join(guessed_word):
                #     # print("You guessed the word!\nYou survived!")
                #     print("""Thanks for playing!
                # We'll see how well you did in the next stage
                # """)
                #     break

            else:
                # attempts_number = attempts_number - 1
                # print('No improvements')
                print("You already typed this letter")
        else:
            attempts_number = attempts_number - 1
            print('No such letter in the word')
            if attempts_number == 0:
                print("You are hanged!")


    else:
        if len(current_letter) != 1:
            print("You should input a single letter")
        else:
            print("It is not an ASCII lowercase letter")
    user_letters.append(current_letter)



# if current_word == "".join(guessed_word):
#     pass
#     # print("You guessed the word!\nYou survived!")
# else:
#     print("You are hanged!")