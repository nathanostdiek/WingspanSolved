# src/entities/habitat.py

class Habitat:
    def __init__(self, name):
        self.name = name
        self.birds = []

    def __repr__(self):
        return f"Habitat(name={self.name}, birds={len(self.birds)})"