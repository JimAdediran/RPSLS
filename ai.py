from player import Player
import random


class AI(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.score = 0

        

    def gesture_choice(self):
        self.gesture_choice = self.gestures[random.randint(0,4)]
        print(f'{self.name} has chosen {self.gesture_choice}')