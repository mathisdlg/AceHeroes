from Game.Database.Database import GameDB
from Functions import *


if __name__ == '__main__':
    db = GameDB()
    db.connect("db.pickle")

    Player_list:list = []
    Player_list = db.loading()
    
    Name_list = []
    if len(Player_list) != 0:
        Name_list = generate_list_name(Player_list)
        
    
    clear_output()

    while True:
        choose = mainMenu()
        
        match choose:
            case 1:
                add_player(Player_list, Name_list)
            case 2:
                suppr_player(Player_list, Name_list)
            case 3:
                print(print_all_player(Name_list), "players")
            case 4:
                display_player(Player_list, Name_list)
            case 5:
                load_all_combine()
            case 6:
                db.backup()
                print("Backup done")
            case 9:
                db.save(Player_list)
                db.disconnect()
                break


        input("Press in enter to continue...")
        clear_output()
    print("See you soon !")