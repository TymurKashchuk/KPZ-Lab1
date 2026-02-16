import random

class Coin:
    def __init__(self):
        self.__sideup = random.choice(["heads", "tails"])

    def toss(self):
        self.__sideup = random.choice(["heads", "tails"])
        return self.__sideup