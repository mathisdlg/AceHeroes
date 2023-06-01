from os.path import exists
from os import mkdir
from pickle import dump, load, loads


class GameDB:
    """
    Ace Heroes database
    """

    def __init__(self):
        
        pass
    
    def connect(self, fileName: str) -> int:
        if exists("data"):
            if exists("data/"+fileName):
                self.file = open("data/"+fileName, "r+b")
                return 0
        else:
            mkdir("data") 
        self.file = open("data/"+fileName, "w+b")
        self.save([])
        return 1
    
    def save(self, objectList: list) -> int:
        self.file.seek(0)
        dump(objectList, self.file)
        return 0
    
    def loading(self) -> list:
        self.file.seek(0)
        data = load(self.file)
        return data
    
    def backup(self) -> None:
        with open("data/backup.pickle", "w+b") as backup:
            dump(loads(self.file.read()), backup)
    
    def load_backup(self, path) -> list:
        with open(path, "r+b") as backup:
            data = load(backup)
        return data
        
    def disconnect(self) -> int:
        self.file.close()
        return 0