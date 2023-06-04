from Game.Player.Class import Class, CLASS_LIST, choose_class
from Game.Player.Race import Race, RACE_LIST, choose_race
from Game.Player.Player import Player
from Game.Player.Skill import Skill
import hashlib as hl
import getpass

from os import system, name 


# Constant
DIFFICULTY_LIST = ["G", "F", "E", "D", "C", "B", "A", "S", "2S", "3S"]
RARITY_LIST = ["G", "F", "E", "D", "C", "B", "A", "S", "2S", "3S"]
MAIN_MENU_CHOICE = {
    1: "Add a player",
    2: "Delete a player",
    3: "Display all player",
    4: "Display a player",
    5: "Display all combine",
    6: "Do a backup",
    9: "Exit"
}


# Genral part
def choose_name(nameList: list[str]) -> str:
    while True:
        name_ = input("Enter your pseudo: ")
        if name_ not in nameList:
            return name_


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

def exitAll(Player_list: list[Player]):
    db.save(Player_list)
    db.disconnect()
    print("Goodbye!")
    exit(0)


def displayList(dico: dict) -> None:
    for key, value in dico.items():
        print(f"{key}: {value}")



# Menu part
def mainMenu():
    displayList(MAIN_MENU_CHOICE)

    while True:
        choose = input("Enter your choice: ")
        
        if not choose.isnumeric():
            print("Please enter a number")
            continue

        choose = int(choose)
        if choose in MAIN_MENU_CHOICE.keys():
            return choose
        else:
            print("Invalid choice")
            continue



# Player part
def add_player(playerList: list[Player], nameList: list[str]) -> None:
    clear_output()
    name = choose_name(nameList)
    
    clear_output()        
    race_chooser = choose_race()
    
    clear_output()
    class_chooser = choose_class()
    
    clear_output()
    while True:
        password: hashlib._Hash.hexdigest = hl.sha256(getpass.getpass("Enter your password: ").encode()).hexdigest()
        confirm = hl.sha256(getpass.getpass("Confirm your password: ").encode()).hexdigest()
        if password == confirm:
            break
        else:
            print("Password not match")
    

    nameList.append(name)
    playerList.append(Player(name, Class(class_chooser), Race(race_chooser), password))
    
    print(f"Welcome to the game {name}!")
    print(f"You are now a {race_chooser} {class_chooser}")


def suppr_player(playerList: list[Player], nameList: list[str]):
    clear_output()
    player_name = input("Enter a player name: ")
    if player_name not in nameList:
        return 1
    else:
        del playerList[nameList.index(player_name)]
        nameList.remove(player_name)
        return 0


def get_player(playerList: list[Player], nameList: list[str]):
    while True:
        name = input("Enter a player name[q to quit]: ")
        if name in nameList:
            return playerList[nameList.index(name)]
        elif name == 'q':
            break
        else:
            print("Player not found")
    return 0



def print_all_player(nameList: list[str]) -> None:
    print("\nPlayer:\n")
    for name in nameList:
        print(name)
    return len(nameList)


def generate_list_name(playerList: list[Player]):
    return [player.get_name() for player in playerList]


def display_player(playerList: list[Player], nameList: list[str]) -> None:
    player: Player = get_player(playerList, nameList)

    if player == 0:
        print("Operation cancelled by the user")
    else:
        player.display()