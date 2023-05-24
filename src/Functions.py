from Game.Player.Class import Class, CLASS_LIST, choose_class
from Game.Player.Race import Race, RACE_LIST, choose_race
from Game.Player.Player import Player
from Game.Player.Skill import Skill

from os import system, name 


DIFFICULTY_LIST = ["G", "F", "E", "D", "C", "B", "A", "S", "2S", "3S"]
RARITY_LIST = ["G", "F", "E", "D", "C", "B", "A", "S", "2S", "3S"]


def choose_name(nameList: list[str]) -> str:
    while True:
        name_ = input("Enter your pseudo: ")
        if name_ not in nameList:
            return name_



def add_player(nameList: list[str], playerList: list[Player]) -> None:
    name = choose_name(nameList)
    
    clear_output()        
    race_chooser = choose_race()
    
    clear_output()
    class_chooser = choose_class()

    nameList.append(name)
    playerList.append(Player(name, Class(class_chooser), Race(race_chooser)))


def suppr_player(nameList: list[str], playerList: list[Player]):
    player_name = input("Enter a player name: ")
    if player_name not in nameList:
        return 1
    else:
        del playerList[nameList.index(player_name)]
        nameList.remove(player_name)
        return 0


def get_player(nameList: list[str], playerList: list[Player]):
    while True:
        name = input("Enter a player name[q to quit]: ")
        if name in nameList:
            return playerList[nameList.index(name)]
        elif name == 'q':
            break
        else:
            print("Player not found")
    return 0


def print_player(Player: Player):
    print(f"{Player.get_name()} is level is {Player.get_level()} and he have {Player.get_stat_point()} stat points\n")


def print_all_player(playerList: list[Player]) -> None:
    print("Player:\n")
    for Player in playerList:
        print_player(Player)
    return len(playerList)


def generate_list_name(playerList: list[Player]):
    return [player.get_name() for player in playerList]



def clear_output() -> None:
    if name == 'nt':
        system('cls')
    else:
        system('clear')



def load_all_combine() -> int:
    i = 0
    for class_ in CLASS_LIST:
        for race_ in RACE_LIST:
            print(f"A {race_} of class: {class_}")
            i+=1
    return i



def display_player(nameList: list[str], playerList: list[Player]) -> None:
    player = get_player(nameList, playerList)

    if player == 0:
        print("Operation cancelled by the user")
    else:
        player_name_long = len(player.nme)-1
        print("\n=============="+"="*(player_name_long))
        print(f"Player name: {player.name}")
        print("--------------"+"-"*(player_name_long))
        print("Health Point: {}".format(player.stats["HP"]))
        print("Mana Point: {}".format(player.stats["MP"]))
        print("Strenght: {}".format(player.stats["STR"]))
        print("Defense: {}".format(player.stats["DEF"]))
        print("Agility: {}".format(player.stats["AG"]))
        print("Dodge: {}".format(player.stats["DODG"]))
        print("Intelligence: {}".format(player.stats["INT"]))
        print("Wisdom: {}".format(player.stats["WIS"]))
        print("Luck: {}".format(player.stats["LUK"]))
        print("=============="+"="*(player_name_long)+"\n")