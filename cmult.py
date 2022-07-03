import ctypes
import pathlib

libname = pathlib.Path().absolute() / "libcmult.so"
c_lib = ctypes.CDLL(libname)
c_lib.cmult.restype = ctypes.c_float

def cmult(a: int, b: float) -> float:
    return c_lib.cmult(a, ctypes.c_float(b))