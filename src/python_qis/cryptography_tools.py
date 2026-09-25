import hashlib
from typing import Literal

def blake2(variant: Literal["b", "s"], data: bytes = b"") -> str:
    """Compute BLAKE2 hash. 'b' for 64-bit (standard), 's' for 32-bit (embedded/IoT)."""
    fn_name = f"blake2{variant}"
    
    # Use getattr with a default of None to safely check existence
    hash_func = getattr(hashlib, fn_name, None)
    
    if not hash_func:
        raise ValueError(f"ERROR: BLAKE2 variant '{variant}' is unsupported.")
        
    return hash_func(data).hexdigest()

def sha3(variant: Literal["256", "512"], data: bytes = b"") -> str:
    """Compute SHA-3 hash. NIST-standardized and quantum-resistant."""
    fn_name = f"sha3_{variant}"
    
    hash_func = getattr(hashlib, fn_name, None)
    
    if not hash_func:
        raise ValueError(f"ERROR: SHA-3 variant '{variant}' is unsupported.")
        
    return hash_func(data).hexdigest()