# msdie.py
#   Class definition for an n-sided die
#   exercise from book for defining classes

from random import randrange
class MSDie:
    def __init__(self, sides):
        self.sides = sides
        self.value = 1
    def roll(self):
        self.value = randrange(1, self.sides+1)
    def getValue(self):
        return self.value
    def setValue(self, value):
        self.value = value
# call to the constructor setting the instance variable die1.value to 1
die1 = MSDie(6)
die1.setValue(8)
print(die1.getValue())