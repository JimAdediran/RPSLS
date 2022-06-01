from time import sleep
from ai import AI
from human import Human
from player import Player

def game_initiate():
    print("Welcome to Rock Paper Scissors Lizard Spock \n")
    sleep(2)
    print("each match will be best of three games \n \n")
    sleep(2)
    print("Use the number keys to enter your selection \n \n \nScissors cuts Paper \nPaper covers Rock \nRock crushes Lizard \
\nLizard poisons Spock \nSpock smashes Scissors \nScissors decapitates Lizard \nLizard eats Paper \nPaper disproves Spock \
\nSpock vaporizes Rock \nRock crushes Scissors \n")

def number_of_players():
    player_number = input("How many players? 1, 2 or 3 for a surprise ")
    if player_number == "1":
        human_vs_ai()       
    elif player_number == "2":
        human_vs_human()
    elif player_number == "3":
        ai_vs_ai()
    else:
        print("Invalid selection, please choose again")
        number_of_players()



    
def human_vs_ai():
    player_one = Human
    player_one_input = int(input("Choose 0 for Rock\n Choose 1 for Paper\n Choose 2 for Scissors\n Choose 3 for Lizard\n Choose 4 for Spock"))

    player_two = AI
    player_two.gesture_choice

def human_vs_human():
    player_one = Human
    player_two = Human

def ai_vs_ai():
    player_one = AI
    player_two = AI
