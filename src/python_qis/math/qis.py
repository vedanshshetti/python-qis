from .general import exponentiation

def is_normalized(vector: list[complex])-> bool:
    absList: list[complex] = []
    for i in vector:
        absList.append(abs(0 - i))
    total = 0
    for i in absList:
        total+= exponentiation(i, 2)
    return True if abs(total - 1.0) < 1e-9 else False

def buildVector(*args: complex)-> list[list[complex]]: 
    v: list[list[complex]] = []
    for i in args:
        v.append([i])
    return v