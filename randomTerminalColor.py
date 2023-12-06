import random
from sty import fg

def generateRGB():
    red = random.randint(0, 256)
    green = random.randint(0, 256)
    blue = random.randint(0, 256)
    return red, green, blue

def changeColor(red, green, blue):
    return fg(red, green, blue)


red, green, blue = generateRGB()
color = changeColor(red, green,blue)



print(color, "COLOR CHANGED!!!")