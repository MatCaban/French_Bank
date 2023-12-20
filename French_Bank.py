from random import randint



def round_sumary(round_sum):
        if round_sum >= 5 and round_sum <= 7:
            print("Low Bet Win!")
        elif round_sum >= 14 and round_sum <= 16:
            print("High Bet Win!")
        elif dice_1.dice_toss() == dice_2.dice_toss() == dice_3.dice_toss():
            print("Ace Bet Win!")
        else:
            print("No one wins, new toss.")

dice_1 = randint(1,6)
dice_2 = randint(1,6)
dice_3 = randint(1,6)
player_name = ""
player_bank = ""
casino_bank = 10000
game_on = True

while game_on:
     break
     
round_sum = dice_1 + dice_2 + dice_3

round_sumary(round_sum)

