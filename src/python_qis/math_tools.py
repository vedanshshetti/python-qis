import math
from decimal import Decimal, getcontext

# Set the decimal limit to 100
getcontext().prec = 100


# Constants
pi_string = "3.1415926535 8979323846 2643383279 5028841971 6939937510 5820974944 5923078164 0628620899 8628034825 3421170679".replace(" ", "")


def add(*args: complex) -> complex: return sum(args)
def subtract(a: complex, b: complex) -> complex: return a - b
def multiply(*args: complex) -> complex: 
    prod = 1
    for i in args:
        prod*=i
    return prod
def divide(a: complex, b: complex) -> complex: return a / b
def exponentiation(a: complex, b: complex) -> complex: return a**b
def factorial(n: int) -> int: 
    if n > 0: return math.factorial(n)
    elif n < 0: raise ValueError("ERROR: factorial(n) n must be a positive integer.")
    else: return 1
def pi(digits: int) -> Decimal: return Decimal(pi_string[0 : len(pi_string) if digits >= len(pi_string) else digits])

def is_normalized(vector: list[complex])-> bool:
    absList: list[complex] = []
    for i in vector:
        absList.append(abs(0 - i))
    total = 0
    for i in absList:
        total+= exponentiation(i, 2)
    return True if abs(total - 1.0) < 1e-9 else False