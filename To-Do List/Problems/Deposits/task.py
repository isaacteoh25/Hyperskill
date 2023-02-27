from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, starting_sum, interest=None):
        self.sum = starting_sum
        self.interest = interest

    @abstractmethod
    def add_money(self, amount):
        ...

    def add_interest(self):
        ...


# create SavingsAccount and Deposit
class SavingsAccount(Account):
    def add_money(self, amount):
        if amount > 10:
            self.sum = self.sum + amount
            # print(self.sum)
        else:
            print("Cannot add to SavingsAccount: amount too low.")



class Deposit(Account):
    def add_money(self, amount):
        if amount > 50:
            self.sum = self.sum + amount
            # print(self.sum)
        else:
            print("Cannot add to Deposit: amount too low.")
    def add_interest(self):
        if self.interest is None:
            self.sum = self.sum
        else:
            self.sum = self.interest * self.sum + self.sum
            # print(self.sum)


# new_savings = SavingsAccount(50)
# new_savings.add_money(5)  # prints the following message:
# # Cannot add to SavingsAccount: amount too low.
# new_savings.add_money(30)
# new_savings.add_interest()
# print(new_savings.sum)
# # 80
#
# new_deposit = Deposit(60, 0.078)
# new_deposit.add_money(30)  # prints the following message:
# # Cannot add to Deposit: amount too low.
# new_deposit.add_money(70)
# new_deposit.add_interest()
# print(new_deposit.sum)
# # 140.14

# class Account(ABC):
#     def __init__(self, starting_sum, interest=None):
#         self.sum = starting_sum
#         self.interest = interest
#
#     @abstractmethod
#     def add_money(self, amount):
#         self.sum += amount
#
#     def add_interest(self):
#         if self.interest is None:
#             return
#         self.sum *= (1 + self.interest)
#
# # create SavingsAccount and Deposit
# class SavingsAccount(Account):
#     def add_money(self, amount):
#         if amount <= 10:
#             print('Cannot add to SavingsAccount: amount too low.')
#         else:
#             self.sum += amount
#
#
# class Deposit(Account):
#     def add_money(self, amount):
#         if amount <= 50:
#             print('Cannot add to Deposit: amount too low.')
#         else:
#             self.sum += amount
