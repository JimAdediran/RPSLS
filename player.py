class Player:
    def __init__(self):
        self.score = 0
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]


    def score_up(self):
        self.score += 1
        