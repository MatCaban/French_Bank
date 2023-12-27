from random import randint
import os

#clear screan
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


#function to decide witch bet wins
def round_sumary(round_sum):
        if round_sum >= 5 and round_sum <= 7:
            print("Low Bet Win!")
            return "a"
        elif round_sum >= 14 and round_sum <= 16:
            print("High Bet Win!")
            return "b"
        elif dice_1 == dice_2 == dice_3:
            print("Ace Bet Win!")
            return "c"
        else:
            print("No one wins, new toss.")
            return "x"
#function that veritify bank balance
def bet_verit(bet, bank):
    while True:
        try:
            bet = input("What is going to be your bet for this round? ")
            bet = int(bet)
            if bet < bank:
                return bet
            else:
                print(f"Sorry, not enough money in your bank. You've got {bank} €")
        except:
            print("Sorry, only numeric value.")
#function that handle player choice:
def player_choice_bet():
    print("For low bet type A\nFor high bet type B\nFor Ace type C")
    while True:
        choice_input = input("What is your choice? ").lower()
        try:
            if choice_input == "a" or choice_input == "b" or choice_input == "c":
                return choice_input
            else:
                print("Sorry, wrong choice, choose only 'A', 'B', 'C'!")
        except:
            print("Sorry, wrong choice, choose only 'A', 'B', 'C'!")



player_name = ""
player_bank = 0
player_bet = 0
player_choice = ""
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

cls()
while True:
    try:
        player_bank = input(f"Hello {player_name}, How much do you want to put in your bank?: ")
        player_bank = int(player_bank)
        break
    except:
        print("Sorry wrong input, we accept value in numbers.")  


while player_bank > 0:
    print(f"Welcome to new round! Your current bank balance is {player_bank}")
    dice_1 = randint(1,6)
    dice_2 = randint(1,6)
    dice_3 = randint(1,6)
    
    player_choice = player_choice_bet()
    player_bet = bet_verit(player_bet, player_bank)
    

    round_sum = dice_1 + dice_2 + dice_3
    print(f"The sum of dices for this round is: {round_sum}")
    if round_sumary(round_sum) == "x":
        continue
    else:
        input_continue = input("Do you want to continue? exit if you want end ")
        if input_continue == "":
            cls()
            continue
        break

