class Mammal:
    def __init__(self):
        self.bio_class = "mammal"

    def greet(self):
        print("I am a {}!".format(self.bio_class))


# create class Dolphin here
class Dolphin(Mammal):
    def __init__(self):
        # self.bio_class = "dolphin"
        # print("I am a {}!".format("dolphin"))
        super().__init__()

        # print("I am a ".format("dolphin"))

    def greet(self):
        print("I am a {}!".format(self.bio_class))
        print("I am a {}!".format("dolphin"))
# class Dolphin(Mammal):
#     def __init__(self):
#         super().__init__()
#         Mammal.greet(self)
#         self.bio_class = 'dolphin'
# class Dolphin(Mammal):
#     def __init__(self):
#         super().__init__()
#         self.greet()
#         self.bio_class = "dolphin"
# class Dolphin(Mammal):
#
#     def greet(self):
#         super().greet()
#         print("I am a dolphin!")

# dolph = Dolphin()
# dolph.greet()


# class Plant:
#     def __init__(self, variety):
#         self.variety = variety
#         print("{} is a plant".format(self.variety))
#
#
# class Cactus(Plant):
#     def __init__(self, variety):
#         super().__init__(variety)
#         print("{} is a cactus".format(self.variety))
#
# opuntia = Cactus("Opuntia")