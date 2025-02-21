# src/entities/game.py

class Game:
    def __init__(self, players):
        self.players = players
        self.round = 1
        self.turn = 0

    def __repr__(self):
        return f"Game(round={self.round}, turn={self.turn})"