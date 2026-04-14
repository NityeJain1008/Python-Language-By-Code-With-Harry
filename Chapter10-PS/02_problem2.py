import math   # needed for square root

class Calculator:

    def __init__(self, num):
        self.num = num   # number stored inside object

    def square(self):
        print("Square =", self.num * self.num)

    def cube(self):
        print("Cube =", self.num * self.num * self.num)

    def square_root(self):
        print("Square root =", math.sqrt(self.num))

a = Calculator(4) ; 

a.square(); 
a.cube ; 
a.square_root ; 