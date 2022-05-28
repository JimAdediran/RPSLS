from player import Player
import random
from time import sleep

class Human(Player):
    def __init__(self, identity, name):
        super().__init__(identity, name)
        self.score = 0
        self.name = name


    def gesture_choice(self):
        self.gesture_choice = int(input())
        gesture_options = ["Rock", "Paper", "Scissors", "Lizards", "Spock"]
