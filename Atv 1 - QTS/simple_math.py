import math

class SimpleMath:
    def sum (self, a, b):
        return a + b
    
    def subtraction (self, a, b):
        return a - b
    
    def multiplication (self, a, b):
        return a * b
    
    def division (self, a, b):
        if b == 0:
            return 0
        return a / b
    
    def mean (self, a, b):
        return (a + b) / 2
    
    def square_root(self, number):
        return math.sqrt(number)
    
