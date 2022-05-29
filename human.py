from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()
        self.victory = 0

    def gesture_choice(self):
        self.gesture_choice = int(input())
        gesture_options = ["Rock", "Paper", "Scissors", "Lizards", "Spock"]
