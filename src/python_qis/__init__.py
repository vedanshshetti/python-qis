import python_qis.math_tools as math_tools
import python_qis.cryptography_tools as cryptography_tools
import python_qis.physics_tools as physics_tools

maths = math_tools
physics_constants: dict[str, complex | float] = {
    "H_JOULE_SEC": physics_tools.H_JOULE_SEC,
    "HBAR_JOULE_SEC": physics_tools.HBAR_JOULE_SEC,
    "BOLTZMANN_CONSTANT": physics_tools.BOLTZMANN_CONSTANT,
    "SPEED_OF_LIGHT": physics_tools.SPEED_OF_LIGHT,
    "ELEMENTARY_CHARGE": physics_tools.ELEMENTARY_CHARGE
}

__all__ = ["maths", "cryptography_tools", "physics_constants"] # Export Everything Here