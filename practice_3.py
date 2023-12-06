class Guitar:
    def __init__(self, color, n_string=6):
        self.n_string = n_string
        self.color = color        

    def play(self):
        print("bumbumbum")

class BassGuitar(Guitar):
    pass

class ElectroGuitar(Guitar):
    def __init__(self, color):
        super().__init__(color, n_string = 8)
    def playLouder(self):
        print("bumbumbum".upper())

my_guitar = Guitar("orange")
my_guitar2 = ElectroGuitar("red")
my_guitar3 = BassGuitar("black", 4)

print(f"Parent Class: {my_guitar.n_string}")
print(f"Child Class: {my_guitar2.n_string}")
print(f"Bass Guitar Class: {my_guitar3.n_string}")
print(f"Electro Guitar string is {my_guitar2.n_string}")
