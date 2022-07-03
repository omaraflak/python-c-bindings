# Python C bindings

Run C code in Python.

# How to

Compile the C library:

```shell
make
```

Use in Python:

```python
from cmult import cmult
assert cmult(5, 1.3) == 6.5
```