from player import Player
import random


class AI(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.score = 0

        

    def gesture_choice(self):
        self.gesture_choice = str(random.randint(0,4))
        self.gestures = ["Rock", "Paper", "Scissors", "Lizards", "Spock"]
        print(f'{self.name} has chosen {self.gesture_choice[int(self.gesture_choice)]}')