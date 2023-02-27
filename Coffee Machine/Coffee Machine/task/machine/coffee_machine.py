class CofeeMachine:
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550

    def remaining(self):
        print(f'''
The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.beans} of coffee beans
{self.cups} of disposable cups
{self.money} of money
''')

    def take_money(self):
        print(f'I gave you ${self.money}')
        self.money = 0

    def fill_machine(self):
        print('Write how many ml of water do you want to add:')
        self.water += int(input())
        print('Write how many ml of milk do you want to add:')
        self.milk += int(input())
        print('Write how many grams of coffee beans do you want to add:')
        self.beans += int(input())
        print('Write how many disposable cups of coffee do you want to add:')
        self.cups += int(input())

    def buy_coffee(self, coffee_type):
        if coffee_type == 1:
            dose_water = 250
            dose_milk = 0
            dose_beans = 16
            dose_money = 4
        elif coffee_type == 2:
            dose_water = 350
            dose_milk = 75
            dose_beans = 20
            dose_money = 7
        elif coffee_type == 3:
            dose_water = 200
            dose_milk = 100
            dose_beans = 12
            dose_money = 6
        if dose_water > self.water:
            print('Sorry, not enough water!')
            return
        elif dose_milk > self.milk:
            print('Sorry, not enough milk')
            return
        elif dose_beans > self.beans:
            print('Sorry, not enough beans')
            return
        self.water -= dose_water
        self.milk -= dose_milk
        self.beans -= dose_beans
        self.money += dose_money
        self.cups -= 1
        print('I have enough resources, making you a coffee!')
    def command_runner(self):
        while True:
            print('Write action (buy, fill, take, remaining, exit)):')
            command = input()
            if command == 'buy':
                print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
                coffee_type = input()
                if coffee_type != 'back':
                    self.buy_coffee(int(coffee_type))
            elif command == 'remaining':
                self.remaining()
            elif command == 'fill':
                self.fill_machine()
            elif command == 'take':
                self.take_money()
            elif command == 'exit':
                break

delonghi = CofeeMachine()
delonghi.command_runner()
# water = int(input("Write how many ml of water the coffee machine has:"))
# milk = int(input("Write how many ml of milk the coffee machine has:"))
# beans = int(input("Write how many grams of coffee beans the coffee machine has:"))

# n = int(input("Write how many cups of coffee you will need:"))
# waterc = water // 200
# milkc = milk // 50
# beansc = beans // 15
# minc =min(waterc,milkc, beansc)
# if n == minc:
#     print("Yes, I can make that amount of coffee")
# elif minc > n:
#     extra = minc - n
#     print(f"Yes, I can make that amount of coffee (and even {extra} more than that)")
# else:
#     print(f"No, I can make only {minc} cups of coffee")
# print(f"""For {n} cups of coffee you will need:
# {200*n} ml of water
# {50*n} ml of milk
# {15*n} g of coffee beans""")