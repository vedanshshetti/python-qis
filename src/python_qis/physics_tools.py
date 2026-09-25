import math

def buildVector(*args: complex)-> list[list[complex]]: 
    v: list[list[complex]] = []
    for i in args:
        v.append([i])
    return v

# Fundamental Constants (SI Units)
H_JOULE_SEC = 6.62607015e-34       # Planck constant
HBAR_JOULE_SEC = H_JOULE_SEC / (2 * math.pi) # Reduced Planck constant
SPEED_OF_LIGHT = 299_792_458       # m/s
BOLTZMANN_CONSTANT = 1.380649e-23  # Joules per Kelvin (J/K)
ELEMENTARY_CHARGE = 1.602176634e-19 # Coulombs (C)

# Standard States (Qubits)
KET_0 = buildVector(1, 0)
KET_1 = buildVector(0, 1)
KET_PLUS = buildVector(1/math.sqrt(2), 1/math.sqrt(2))
BELL_PHI_PLUS = buildVector(1/math.sqrt(2), 0, 0, 1/math.sqrt(2))