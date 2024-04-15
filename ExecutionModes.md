# How Python sees the World

## Execution modes

Play through hello world in different ways:

* [x] REPL
* [x] VSCODE script
* [x] VSCODE notebook

Anecdata: After many years, I find the REPL still very useful for ad-hoc
exploration. Mostly with IPython, which allows to run benchmarks, lookup docs,
export to scripts, etc.

## Physical Design

* the interpreter is a single "C" program that reads scripts line-by-line and either
compiles blocks (functions, classes) or executes statements (init, compile, interpret)
* python uses a VM that runs bytecode
* python uses a GC
* all code is converted to bytecode in one form or another

```python
In [1]: import dis

In [2]: def hello(name="world"):
   ...:     print(f"hello {name}")
   ...:

In [3]: dis.dis(hello)
  2           0 LOAD_GLOBAL              0 (print)
              2 LOAD_CONST               1 ('hello ')
              4 LOAD_FAST                0 (name)
              6 FORMAT_VALUE             0
              8 BUILD_STRING             2
             10 CALL_FUNCTION            1
             12 POP_TOP
             14 LOAD_CONST               0 (None)
             16 RETURN_VALUE
```

* you may see "cached" files with the ".pyc" extension
  ([SO2998215](https://stackoverflow.com/questions/2998215/if-python-is-interpreted-what-are-pyc-files)),
these can be safely deleted at any time as they are just an optimization (can be suppresed via `-B` or via `PYTHONDONTWRITEBYTECODE=dontcare`
* there are [over 200](https://github.com/python/cpython/blob/a2ae84726b8b46e6970ae862244dad1a82cf5d19/Include/opcode_ids.h#L12-L234) opcodes

```python
>>> import dis
>>> code = compile("x = 1", "dummy.py", "single")
>>> bc = dis.Bytecode(code)
>>> print(bc.dis())
  1           0 LOAD_CONST               0 (1)
              2 STORE_NAME               0 (x)
              4 LOAD_CONST               1 (None)
              6 RETURN_VALUE
>>> exec(code)
>>> x
1
```

* python comes with a standard library
* code can be loaded from other locations ("site-packages"), etc.

```python
# modules
import sys
print(sys.modules)
```

A plain script on Linux using Python 3.10 imports 76 modules before user code runs.

## Where does Python code come from?

When you try to import Python code, it will look for code in `sys.path`, which may look like this:

```python
In [1]: import sys

In [2]: sys.path
Out[2]:
['/home/tir/.local/bin',
 '/usr/lib/python310.zip',
 '/usr/lib/python3.10',
 '/usr/lib/python3.10/lib-dynload',
 '',
 '/home/tir/.local/lib/python3.10/site-packages',
 '/usr/local/lib/python3.10/dist-packages',
 '/usr/lib/python3/dist-packages']
```

These are mostly directories, and notably, a zip file. These locations do not
have to exists, it is just where python would look, top-to-bottom.

> Initialized from the environment variable PYTHONPATH, plus an
> installation-dependent default. --
> [sys.html#sys.path](https://docs.python.org/3/library/sys.html#sys.path)

A very common error is "ModuleNotFoundError", like:

```
In [18]: import tensorflow as tf
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In [18], line 1
----> 1 import tensorflow as tf

ModuleNotFoundError: No module named 'tensorflow'
```

This does not necessary mean that the code is not on you machine, it just
cannot be found. You can manipulate sys.path, which is just a list of strings,
but typically programs should not depend on that (try to find the root cause
first).

To see, from where a module has been loaded, check `__file__` attribute of
module.

```
In [22]: import pandas

In [23]: pandas.__file__
Out[23]: '/home/tir/.local/lib/python3.10/site-packages/pandas/__init__.py'
```

If you install code with e.g. "pip", the tool will download and extract code so
that the python interpreter can find it.

