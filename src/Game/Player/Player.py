from Game.Player.Class import Class
from Game.Player.Race import Race
from Game.Player.Clan import Clan


class Player:
    """
    Player:
        - name
        - Classe
        - Race
        - Level
        - Stat point
        - Statistics:
            - HP
            - MP
            - Strength
            - Defense
            - Agility
            - Dodge
            - Intelligence
            - Wisdom
            - Luck
        - clan

    """
    def __init__(self, playerName: str, classe: Class, race: Race):
        self.name: str = playerName
        self.classe: Class = classe
        self.race: Race = race
        self.level: int = 0
        self.stat_point: int = 0
        self.stats: dict = {"HP": 100, "MP": 10, "STR": 1, "DEF":10, "AG": 1, "DODG": 1, "INT": 1, "WIS": 1, "LUK": 1}
        self.hiddenStats: dict = {"ATKRNG": 1}
        self.clan: Clan|None = None
    
    def __str__(self) -> str:
        return self.name
    
    def __format__(self, __format_spec: str) -> str:
        return self.name


    ########################################################
    #                   Get method                         #
    def get_name(self) -> str:
        return self.name
    
    def get_class(self) -> Class:
        return self.classe
    
    def get_race(self) -> Race:
        return self.race
    
    def get_level(self) -> int:
        return self.level
    
    def get_stat_point(self) -> int:
        return self.stat_point
    
    def get_stats(self) -> dict:
        return self.stats
    
    def get_clan(self) -> Clan:
        return self.clan
    ########################################################


    ########################################################
    #                   Set method                         #
    def set_clan(self, clan: Clan) -> None:
        self.clan = clan
    
    def win_stats(self, stats: str, sup: int) -> None:
        self.stats[stats] += sup
    
    def win_level(self, nb: int) -> None:
        self.level += nb
    
    def win_stat_point(self, nb: int) -> None:
        self.stat_point += nb
    ########################################################


    ########################################################
    #                   Other methods                      #
    def duel(self, opponent: "Player"):
        pass #TODO
    
    def talk(self, reciver: "Player"):
        pass
    
    def display(self):
        player_name_long = len(self.name)-1
        player_stats = self.stats

        print("\n=============="+"="*(player_name_long))
        print(f"Player name: {self.name}")
        print("--------------"+"-"*(player_name_long))
        print("Health Point: {}".format(player_stats["HP"]))
        print("Mana Point: {}".format(player_stats["MP"]))
        print("Strenght: {}".format(player_stats["STR"]))
        print("Defense: {}".format(player_stats["DEF"]))
        print("Agility: {}".format(player_stats["AG"]))
        print("Dodge: {}".format(player_stats["DODG"]))
        print("Intelligence: {}".format(player_stats["INT"]))
        print("Wisdom: {}".format(player_stats["WIS"]))
        print("Luck: {}".format(player_stats["LUK"]))
        print("=============="+"="*(player_name_long)+"\n")
    ########################################################