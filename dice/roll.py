from random import random
def roll(sides):
    sides -= 1
    return round(random() * sides )+ 1
    
rolled = roll(6)
print(rolled)

name = {}
name['cell'] = "207.2.2.2"
print(name)
name['ccode'] = rolled
print(rolled)
