# python-qis

Small Python utilities for mathematics, quantum information science, cryptography,
and introductory physics.

## Requirements

- Python 3.13 or newer

## Installation

Install the latest release from PyPI with pip:

```bash
python -m pip install python-qis
```

Or add it to a project managed with uv:

```bash
uv add python-qis
```

## Quick start

### Cryptography

Hash functions accept bytes and return hexadecimal strings:

```python
from python_qis.cryptography_tools import blake2, sha3

message = b"hello, QIS world"

print(blake2("b", message))
print(sha3("256", message))
```

### Math and quantum states

```python
from python_qis import general_math, qis_math

print(general_math.add(2, 3, 5))
print(general_math.pi(12))

state = qis_math.buildVector(1 / 2**0.5, 1 / 2**0.5)
print(qis_math.is_normalized([value[0] for value in state]))
```

### Physics constants and standard states

```python
from python_qis import physics_constants
from python_qis.physics_tools import BELL_PHI_PLUS, KET_0, KET_1, KET_PLUS

print(physics_constants["SPEED_OF_LIGHT"])
print(KET_0, KET_1, KET_PLUS, BELL_PHI_PLUS)
```

## What's included?

- **Math utilities:** arithmetic helpers, factorials, and decimal digits of pi.
- **Quantum information utilities:** vector construction and normalization checks.
- **Cryptography utilities:** BLAKE2 and SHA-3 hashing through Python's standard library.
- **Physics utilities:** selected SI constants and common qubit states.

## Development

Clone the repository and install it in an editable environment:

```bash
git clone https://github.com/VedanshShetti/python-qis.git
cd python-qis
uv sync
```

Build the package with:

```bash
uv build
```

## License

This project is licensed under the terms in [LICENSE](LICENSE).
