chicken = 23
goat = 678
pig = 1296
cow = 3848
sheep = 6769

user_money = int(input())

if user_money >= sheep:
    print(user_money // sheep, "sheep")
elif sheep > user_money >= cow:
    print("1 cow")
elif cow > user_money >= pig:
    if user_money // pig >= 2:
        print(user_money // pig, "pigs")
    else:
        print(" 1 pig")
elif pig > user_money >= goat:
    print(" 1 goat")
elif goat > user_money >= chicken:
    if user_money // chicken >= 2:
        print(user_money // chicken, "chickens")
    else:
        print("1 chicken")
else:
    print("None")