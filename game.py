from time import sleep

def game_initiate():
    print("Welcome to Rock Paper Scissors Lizard Spock \n")
    sleep(2)
    print("each match will be best of three games \n \n")
    sleep(2)
    print("Use the number keys to enter your selection \n \n \nScissors cuts Paper \nPaper covers Rock \nRock crushes Lizard \
\nLizard poisons Spock \nSpock smashes Scissors \nScissors decapitates Lizard \nLizard eats Paper \nPaper disproves Spock \
\nSpock vaporizes Rock \nRock crushes Scissors \n")

def number_of_players():
    sleep(2)
    print("How many players? 1, 2 or 3 for a surprise")
    player_number = input()

    

