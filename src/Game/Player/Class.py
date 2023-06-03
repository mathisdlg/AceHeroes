CLASS_LIST = ['Thief', 'Priest', 'Mage', 'Figther', 'Paladin', 'Ranger', 'Druid', 'Black Mage', 'Labyrinths Master', 'Berserker', 'Assassin', 'Bard', 'Cleric', 'Hunter', 'Villager', 'Beast Master', 'Artificer', 'Craftsman', 'Alchemist', 'Wizard', 'Bettor', 'Dragon Slayer', 'Blacksmith', 'Necromancer', 'Elementalist', 'Ninja', 'Monk', 'Crusader', 'Demolitionist']


def display_classes() -> None:
    for classe in CLASS_LIST:
        print(f"{classe}")

def choose_class() -> "Class":
    while True:
        class_ = input("Enter your class[h to see all classes]: ")
        if class_ in CLASS_LIST:
            return class_
        elif class_ == 'h':
            display_classes()
        else:
            print(f"Invalid class: {class_} not found!")



class Class:
    """
    The differnt class of the game
    """
    def __init__(self, name: str):
        self.class_name = name
        self.class_level = 0