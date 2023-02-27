import random
import sqlite3
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS card')
cur.execute("CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);")
cur.execute('SELECT * FROM card')
j = 0
conn.commit()
print(cur.fetchall())


class Account:

    def __init__(self):
        self.list_of_account = {}
        self.key = None
        self.pin = None
        self.balance = 0

    def new_account(self):
        self.key = "400000" + ''.join([str(random.randint(0, 9)) for _ in range(9)])
        odd = ([self.key[i] for i in range(len(self.key)) if i % 2 == 0])
        double_odd_c = ([int(i) * 2 for i in odd if int(i) * 2 < 10])
        c = sum(double_odd_c)  # double odd_cifre
        double_odd_n = ([int(i) * 2 - 9 for i in odd if int(i) * 2 >= 10])
        n = sum(double_odd_n)  # double odd_number
        p = sum([int(self.key[i]) for i in range(len(self.key)) if i % 2 != 0])  # par
        for i in range(0, 9):
            if (c + n + p + i) % 10 == 0:
                ck = i  # check_nr
                self.key = self.key + str(ck)
            else:
                cur.execute(f"DELETE FROM card WHERE number=({self.key});")
                conn.commit()

        self.pin = ''.join([str(random.randint(0, 9)) for _ in range(4)])
        self.list_of_account[self.key] = self.pin
        global j
        if len(self.key) == 16:
            j += 1
            cur.execute(f'INSERT INTO card (id, number, pin, balance) VALUES ({j}, {self.key}, {self.pin}, 0);')
            conn.commit()
            return print(f"Your card has been created\nYour card number:\n{self.key}\nYour card PIN:\n{self.pin}\n")
        else:
            new.new_account()

    def check_if_exist(self, key_, pin_):
        if key_ in self.list_of_account and self.list_of_account[key_] == pin_:
            return "You have successfully logged in!"
        else:
            return print("\nWrong card number or PIN!\n")

    def check_balance(self):
        return print(f"\nBalance: {self.balance}")

    def add_income(self):
        self.key = key_
        self.pin = pin_
        new_income = int(input('\nEnter income:\n'))
        new.balance += new_income
        cur.execute(f"UPDATE card SET balance=({new.balance}) WHERE number=({self.key});")
        conn.commit()
        return print('Income was added!\n')

    def do_transfer(self):

        transfer_card = input('Enter card number:\n')
        if transfer_card in self.list_of_account:
            if transfer_card == key_:
                print('Please choose another card!\n')
            elif transfer_card != key_:
                transfer_sum = int(input('Enter how much money you want to transfer:\n'))
                if transfer_sum > new.balance:
                    return print('Not enough money!')
                else:
                    rest = new.balance - transfer_sum
                    new_sum = transfer_sum
                    cur.execute(f"UPDATE card SET balance=({rest}) WHERE number=({self.key});")
                    cur.execute(f"UPDATE card SET balance=({new_sum}) WHERE number=({transfer_card});")
                    conn.commit()
                    return print("Success!")

        elif transfer_card not in self.list_of_account:
            print('Probably you made a mistake in the card number. Please try again!')
            transfer_card = input('Enter card number:\n')
            if transfer_card not in self.list_of_account:
                return print('Such a card does not exist.')

    def close_account(self):
        cur.execute(f"DELETE FROM card WHERE number=({self.key});")
        conn.commit()
        self.list_of_account[key_] = 'closed'
        return print('\nThe account has been closed!\n')

    def log_out(self):
        return print('\b\b')


new = Account()

choice = None
while choice != 0:
    print("1. Create an account\n2. Log into account\n0. Exit\n")
    choice = int(input())
    if choice == 1:
        new.new_account()
    elif choice == 2:
        key_ = input("Enter your card number:\n")
        pin_ = input("Enter your PIN:\n")
        if (new.check_if_exist(key_, pin_)) == "You have successfully logged in!":
            print("\nYou have successfully logged in!")
            while True:
                print("\n1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit\n")
                choice_ = int(input())
                if choice_ == 1:
                    new.check_balance()
                if choice_ == 2:
                    new.add_income()
                if choice_ == 3:
                    new.do_transfer()
                if choice_ == 4:
                    new.close_account()
                    break
                if choice_ == 5:
                    new.log_out()
                    break
                if choice_ == 0:
                    print("Bye!")
                    quit()
    elif choice == 3:
        print("\nBye!")
        break