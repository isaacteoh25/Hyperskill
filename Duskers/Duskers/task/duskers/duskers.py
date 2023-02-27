def main_screen():
    print("""██████╗ ██╗   ██╗███████╗██╗  ██╗███████╗██████╗ ███████╗
██╔══██╗██║   ██║██╔════╝██║ ██╔╝██╔════╝██╔══██╗██╔════╝
██║  ██║██║   ██║███████╗█████╔╝ █████╗  ██████╔╝███████╗
██║  ██║██║   ██║╚════██║██╔═██╗ ██╔══╝  ██╔══██╗╚════██║
██████╔╝╚██████╔╝███████║██║  ██╗███████╗██║  ██║███████║
╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝""")
    print("""\n\n[Play]
[High] Scores
[Help]
[Exit]""")
    print("Your command:")


# Write your code here
main_screen()


def yes():
    global command
    print("║────────────────────────────────────────────────────────────────────────────────║")
    print("░░██░░░░██░░░░██░░░░██░░░░██░░░░██░░")
    print("░░░██░░██░░░░░░██░░██░░░░░░██░░██░░░")
    print("░░░░████░░░░░░░░████░░░░░░░░████░░░░")
    print("░░░░████░░░░░░░░████░░░░░░░░████░░░░")
    print("░░████████░░░░████████░░░░████████░░")
    print("░██░██░█░░█░░██░██░█░░█░░██░██░█░░█░")
    print("██░░█░░█░░██ ██░░█░░█░░██ ██░░█░░█░░██ ")
    print("║════════════════════════════════════════════════════════════════════════════════║")
    print("║                  [Ex]plore                          [Up]grade                  ║")
    print("║                  [Save]                             [M]enu                     ║")
    print("║════════════════════════════════════════════════════════════════════════════════║")
    print("\n\nYour command:")
    command = input().lower()
    if command == 'm':
        menu()

        if command== 'back':
            yes()
        elif command == 'main':
            main_screen()
        elif command == 'save':
            save()
        # else:
        #     pass
            # break
        elif command == 'ex':
            # main_screen()
            # main_screen()
            print("Thanks for playing, bye!")
        #     break
        #     break
    elif command =='save':
        save()


def menu():
    global command
    print("""                             ║════════════════════════║
                             ║           MENU         ║
                             ║                        ║
                             ║[Back] to game          ║
                             ║ Return to [Main] Menu  ║
                             ║[Save] and exit         ║
                             ║[Exit] game             ║
                             ║════════════════════════║""")
    command = input().lower()


def save():
    print("Coming SOON! Thanks for playing!")


def menus():
    global command
    # while True:
    command = input().lower()
    if command == "play":
        print("Enter your name:")
        b = input()
        print(f"""Greetings, commander {b}!
    Are you ready to begin?
        [Yes] [No]""")
        print("\nYour command:")
        play()
    elif command == "high":
        print("""No scores to display.
[Back]""")
        main_screen()

    elif command == "exit":
        print("Thanks for playing, bye!")

    elif command == "help":
        print("Coming SOON! Thanks for playing!")
    else:
        pass


def play():
    global command
    command = input().lower()
    if command == 'yes':
        yes()
    elif command == "no":
        print("""How about now.
            Are you ready to begin?
                [Yes] [No]""")
        play()


menus()

# print("Great, now let's go code some more ;)")
    # print("Your command:")
    # c = input()
    # print("Great, now let's go code some more ;)")

