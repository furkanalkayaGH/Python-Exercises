class Fruit:
    def __init__(self, name, piece, color, isRound):
        self.name = name
        self.piece = piece
        self.color = color
        self.isRound = isRound

    def details(self):
        if(self.isRound  == True):
            return print(f"My {self.name} is {self.color}, it's {self.piece} of them and it's round") 
        elif(self.isRound == False):
            return print(f"My {self.name} is {self.color}, it's {self.piece} of them and it's not round") 
        else:
            return None
        
apple = Fruit("apple", 1, "red", True)
banana = Fruit("banana",3, "yellow", False)

apple.details()
banana.details()

            
 