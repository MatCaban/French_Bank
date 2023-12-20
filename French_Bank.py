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

round_sum = dice_1.dice_toss() + dice_2.dice_toss() + dice_3.dice_toss()

if round_sum >= 5 and round_sum <= 7:
    print("Low Bet Win!")
elif round_sum >= 14 and round_sum <= 16:
    print("High Bet Win!")
elif dice_1.dice_toss() == dice_2.dice_toss() == dice_3.dice_toss():
    print("Ace Bet Win!")
else:
    print("No one wins, new toss.")
