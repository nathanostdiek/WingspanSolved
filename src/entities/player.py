# src/entities/player.py

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.resources = {'food': [], 'eggs': 0}
        self.score = 0

    def __repr__(self):
        return f"Player(name={self.name}, score={self.score})"