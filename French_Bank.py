from random import randint

#class for dice
class Dice:
    def __init__(self, name):
        self.name = name
    #random number generator for our dice
    def dice_toss(self):
        return randint(1,6)
    


dice_1 = Dice("1")
dice_2 = Dice("2")
dice_3 = Dice("3")

print(dice_1.dice_toss())

#print(f"Value of dice 1 is {dice_1} , value of dice 2 is {dice_2}, value of dice 3 is {dice_3}")
