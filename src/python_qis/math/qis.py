from .general import exponentiation
from random import uniform
from python_qis.types import Vector

def is_normalized(vector: Vector)-> bool:
    absList: list[complex] = []
    for i in vector:
        for n in i:
            absList.append(abs(0 - n))
    total = 0
    for i in absList:
        total+= exponentiation(i, 2)
    return True if abs(total - 1.0) < 1e-9 else False

def buildVector(*args: complex)-> Vector: 
    v: Vector = []
    for i in args:
        v.append([i])
    return v


def measure(vector: Vector) -> tuple[int, Vector]:
    if not is_normalized(vector): raise ValueError("ERROR: measure(...) requires a normalized vector (sum of squared magnitudes must be 1).")

    flattened = []
    for sublist in vector:
        for n in sublist: flattened.append(n)
    
    probabilities = [abs(n) ** 2 for n in flattened]

    cumulative = []
    total = 0
    for p in probabilities:
        total += p
        cumulative.append(total)

    r = uniform(0.0, 1.0)
    winner_index = 0
    for i, val in enumerate(cumulative):
        if r <= val:
            winner_index = i
            break

    new_vector: Vector = []
    for i in range(len(flattened)):
        if i == winner_index: new_vector.append([1])
        else: new_vector.append([0])

    return winner_index, new_vector