from random import randint



def round_sumary(round_sum):
        if round_sum >= 5 and round_sum <= 7:
            print("Low Bet Win!")
        elif round_sum >= 14 and round_sum <= 16:
            print("High Bet Win!")
        elif dice_1 == dice_2 == dice_3:
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

print("""Hello! Welcome to our game of French Bank.
      Game is fairly easy. We are going to toss 3 dices each round.
      Then we will sum points on dices. There are three possible bets, you can make.
      Low bet: sum is 5, 6, 7
      High bet: sum is 14, 15, 16
      Ace is when all 3 dices show same number.
      Winning Low or High bet will earn you 2x your bet.
      Winning Ace will earn you 61x your bet!!!!!!
      Wohooo, let's play!""")

player_name = input("What is your name?: ")

while True:
    try:
        player_bank = input("How much do you want to put in your bank?: ")
        int(player_bank)
        break
    except:
        print("Sorry wrong input, we accept valu in numbers.")  

round_sum = dice_1 + dice_2 + dice_3

round_sumary(round_sum)

