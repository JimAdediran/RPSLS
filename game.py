from curses.ascii import FS
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
    player_one = Human("Joe")
    player_one_decision = player_one.gesture_choice
    player_two = AI("John")
    player_two_decision = player_two.gesture_choice

    while player_one.score < 3 and player_two.score < 3:
        print("Choose 0 for Rock\n Choose 1 for Paper\n Choose 2 for Scissors\n Choose 3 for Lizard\n Choose 4 for Spock")
        player_one_decision()
        player_two_decision()
        if player_one.gesture_choice == "Rock" and player_two.gesture_choice == "Scissors":
            player_one.score_up()
            print("Player one is the winner!")
            sleep(1) 
        elif player_one.gesture_choice == "Rock" and player_two.gesture_choice == "Lizard":
            player_one.score_up()
            print("Player one is the winner!")
            sleep(1)  
        elif player_one.gesture_choice == "Scissors" and player_two.gesture_choice == "Paper":
            player_one.score_up()
            print("Player one is the winner!")
            sleep(1) 
        elif player_one.gesture_choice == "Scissors" and player_two.gesture_choice == "Lizard":
            player_one.score_up()
            print("Player one is the winner!")
            sleep(1) 
        elif player_one.gesture_choice == "Paper" and player_two.gesture_choice == "Rock":
            player_one.score_up()
            print("Player one is the winner!")
            sleep(1) 
        elif player_one.gesture_choice == "Paper" and player_two.gesture_choice == "Spock":
            player_one.score_up()
            print("Player one is the winner!")
            sleep(1) 
        elif player_one.gesture_choice == "Lizard" and player_two.gesture_choice == "Spock":
            player_one.score_up()
            print("Player one is the winner!")
            sleep(1) 
        elif player_one.gesture_choice == "Lizard" and player_two.gesture_choice == "Paper":
            player_one.score_up()
            print("Player one is the winner!")
            sleep(1) 
        elif player_one.gesture_choice == "Spock" and player_two.gesture_choice == "Scissors":
            player_one.score_up()
            print("Player one is the winner!")
            sleep(1) 
        elif player_one.gesture_choice == "Spock" and player_two.gesture_choice == "Rock":
            player_one.score_up()
            print("Player one is the winner!")
            sleep(1) 
        elif player_two.gesture_choice == "Rock" and player_one.gesture_choice == "Scissors":
            player_two.score_up()
            print("Player two is the winner!")
            sleep(1) 
        elif player_two.gesture_choice == "Rock" and player_one.gesture_choice == "Lizard":
            player_two.score_up()
            print("Player two is the winner!")
            sleep(1) 
        elif player_two.gesture_choice == "Scissors" and player_one.gesture_choice == "Paper":
            player_two.score_up()
            print("Player two is the winner!")
            sleep(1) 
        elif player_two.gesture_choice == "Scissors" and player_one.gesture_choice == "Lizard":
            player_two.score_up()
            print("Player two is the winner!")
            sleep(1) 
        elif player_two.gesture_choice == "Paper" and player_one.gesture_choice == "Rock":
            player_two.score_up()
            print("Player two is the winner!")
            sleep(1) 
        elif player_two.gesture_choice == "Paper" and player_one.gesture_choice == "Spock":
            player_two.score_up()
            print("Player two is the winner!")
            sleep(1) 
        elif player_two.gesture_choice == "Lizard" and player_one.gesture_choice == "Spock":
            player_two.score_up()
            print("Player two is the winner!")
            sleep(1) 
        elif player_two.gesture_choice == "Lizard" and player_one.gesture_choice == "Paper":
            player_two.score_up()
            print("Player two is the winner!")
            sleep(1) 
        elif player_two.gesture_choice == "Spock" and player_one.gesture_choice == "Scissors":
            player_two.score_up()
            print("Player two is the winner!")
            sleep(1) 
        elif player_two.gesture_choice == "Spock" and player_one.gesture_choice == "Rock":
            player_two.score_up()
            print("Player two is the winner!")
            sleep(1) 
        elif player_one.gesture_choice == player_two.gesture_choice:
            print("It's a tie!") 
            sleep(1)
        if player_one.score < 3 and player_two.score < 3:
            print("\n \n \n \n \nNext round, first player to win twice is the winner")
        
    
    option = True

    while option == True:
        if player_one.score == 3:
            print ("\nPlayer 1 wins best of 3!")
            option = False
        else:
            print("\nPlayer 2 wins best of 3!")
            option = False


    replay = True    
    while replay == True:
        status = input("\nWould you like to play again? (y/n): ")
        if status == "y":
            replay = False
            human_vs_ai()
        elif status == "n":
            replay = False
        else:
            print("Invalid Selection")
        
        

    

def human_vs_human():
    player_one = Human
    player_two = Human

def ai_vs_ai():
    player_one = AI
    player_two = AI
