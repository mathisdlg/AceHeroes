from os.path import exists
from os import mkdir
from pickle import dump, load


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
    
    def save(self, object: list) -> int:
        self.file.seek(0)
        dump(object, self.file)
        self.file.truncate()
        return 0
    
    def loading(self) -> list:
        self.file.seek(0)
        thing = load(self.file)
        return thing
        
    def disconnect(self) -> int:
        self.file.close()
        return 0


if __name__ == "__main__":
    pass