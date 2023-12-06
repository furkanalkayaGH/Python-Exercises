class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def details(self):
        print(f"My {self.name} is {self.color}")


apple = Fruit("apple", "red")
banana = Fruit("banana", "yellow")
kiwi = Fruit("kiwi", "green")

apple.details()
banana.details()



#print(f"Our fruit name is {apple.name} and it's color is {apple.color}")
#print(f"Our next fruit name is {banana.name} and it's color is {banana.color}")