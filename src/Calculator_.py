import math

def addition(a, b):
    a = int(a)
    b = int(b)
    c = a + b
    return c

def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c

def multiplication(a, b):
    a = int(a)
    b = int(b)
    c = a * b
    return c

def division(a, b):
    a = int(a)
    b = int(b)
    c = float(b / a)
    return c

def square(a):
    a = int(a)
    c = a * a
    return c

def sqroot(a):
    a = int(a)
    c = round(math.sqrt(a), 7)
    return c


class Calculator:
    result = 0

def __init__(self):
    pass

def addit(self, a, b):
    self.result = addition(a, b)
    return self.result

def subt(self, a, b):
        self.result = subtraction(a, b)
        return self.result

def multi(self, a, b):
        self.result = multiplication(a, b)
        return self.result

def divi(self, a, b):
        self.result = round(division(a, b), 9)
        return self.result

def squaredig(self, a):
        self.result = square(a)
        return self.result

def square_root(self, a):
        self.result = sqroot(a)
        return self.result