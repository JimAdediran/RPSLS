from player import Player
import random
from time import sleep

class AI(Player):
    def __init__(self, identity, name):
        super().__init__(identity, name)


    def gesture_choice(self):
        self.gesture_choice = str(random.randint(0,4))
        gesture_options = ["Rock", "Paper", "Scissors", "Lizards", "Spock"]