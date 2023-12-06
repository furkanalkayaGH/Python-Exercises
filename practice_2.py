class Guitar:
    def __init__(self):
        self.n_string = 6
        self.play()

    def play(self):
        print("bumbumbum")


class ElectroGuitar(Guitar):
    pass


my_guitar = Guitar()

my_guitar.play()
print(my_guitar.n_string)

