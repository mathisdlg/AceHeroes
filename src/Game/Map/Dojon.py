class Donjon:
    
    def __init__(self, name: str, level: str, rarity: str, nbMaxPlayers: int):
        self.name = name
        self.level = level
        self.rarity = rarity
        self.nbMaxPlayers = nbMaxPlayers
    
    def try_it(self, player_list):
        pass