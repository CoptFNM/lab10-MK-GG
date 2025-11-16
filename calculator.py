# https://github.com/CoptFNM/lab10-MK-GG

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def multiply(a, b):
    return mul(a, b)

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def divide(a, b):
    return div(a, b)

def exp(x, base):
    if base <= 0 or base == 1:
        raise ValueError("Base must be positive and not equal to 1.")
    if x <= 0:
        raise ValueError("Argument must be positive.")
    return math.log(x, base)

def logarithm(x, base):
    return exp(x, base)

def hypotenuse(a, b):
    return math.hypot(a, b)

def square_root(x):
    if x < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(x)
