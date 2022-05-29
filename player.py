class Player:
    def __init__(self):
        self.score = 0
        self.name = ""
        self.gestures = ["rock", "paper", "scissors", "lizard", "spock"]
        self.chose_gesture = ""

    def score_up(self):
        self.score += 1
        