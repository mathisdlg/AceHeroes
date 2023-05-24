STATE_LIST = ["opened", "closed", "invited", "complet"]

class Clan:
    
    def __init__(self, name:str, master):
        self.name = name
        self.master = master
        self.experince = 0
        self.level = 0
        self.placesMax = 10
        self.list_players = [master]


    ########################################################
    #                   Get method                         #
    def get_name(self) -> str:
        return self.name
    
    def get_master(self):
        return self.master
    
    def get_experince(self) -> int:
        return self.experince
    
    def get_level(self) -> int:
        return self.level
    
    def _get_place(self) ->int:
        return self.placesMax
    
    def get_free_place(self) -> tuple:
        return (self._get_place() - len(self.list_players), self._get_place())
    
    def get_list_players(self) -> list:
        return self.list_players
    ########################################################


    ########################################################
    #                   Set method                         #
    def add_player(self, player) -> int:
        if player in self.list_players:
            return 1
        elif player.get_clan() == None:
            self.list_players.append(player)
            player.set_clan(self.name)
            return 0
        else:
            return 4
    
    def remove_player(self, player) -> int:
        if player in self.list_players:
            self.list_players.remove(player)
            return 0
        else:
            return 2
        
    def set_state(self, state: str) -> int:
        if state in STATE_LIST:
            self.state = state
            return 0
        else: 
            return 3
    ########################################################