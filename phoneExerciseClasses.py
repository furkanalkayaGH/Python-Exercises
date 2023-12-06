class Phone:
    def __init__(self, brand):
        self.brand = brand
        self.sim = 1
    
    def call(self):
        print("Calling...")

class Iphone(Phone):
    def __init__(self, brand):
        super().__init__(brand)
        self.sim = 2
    
my_phone = Phone("Samsung")
my_phone_2 = Iphone("Apple")

print(f"My phone's brand is {my_phone.brand}, There are {my_phone.sim} sim inputs.")
my_phone.call()
print(f"My phone's brand is {my_phone_2.brand}, There are {my_phone_2.sim} sim inputs.")
my_phone_2.call()
