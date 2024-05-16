import ctypes
import pathlib

libname = pathlib.Path().absolute() / "libcmult.so"
c_lib = ctypes.CDLL(libname)

c_lib.cmult.restype = ctypes.c_float
c_lib.cmult.argtypes = [ctypes.c_float, ctypes.c_float]


def cmult(a: float, b: float) -> float:
    return c_lib.cmult(ctypes.c_float(a), ctypes.c_float(b))