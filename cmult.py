import ctypes

c_lib = ctypes.CDLL("libcmult.so")
c_lib.cmult.restype = ctypes.c_float

def cmult(a: int, b: float) -> float:
    return c_lib.cmult(a, ctypes.c_float(b))