import python_qis.math.general as general_math
import python_qis.math.qis as qis_math
import python_qis.cryptography_tools as cryptography_tools
import python_qis.physics_tools as physics_tools
from typing import Literal

physics_constants: dict[
    Literal[
        "H_JOULE_SEC",
        "HBAR_JOULE_SEC",
        "BOLTZMANN_CONSTANT",
        "SPEED_OF_LIGHT", 
        "ELEMENTARY_CHARGE"
    ], complex | float] = {
    "H_JOULE_SEC": physics_tools.H_JOULE_SEC,
    "HBAR_JOULE_SEC": physics_tools.HBAR_JOULE_SEC,
    "BOLTZMANN_CONSTANT": physics_tools.BOLTZMANN_CONSTANT,
    "SPEED_OF_LIGHT": physics_tools.SPEED_OF_LIGHT,
    "ELEMENTARY_CHARGE": physics_tools.ELEMENTARY_CHARGE
}

__all__ = ["qis_math", "general_math", "cryptography_tools", "physics_constants"] # Export Everything Here