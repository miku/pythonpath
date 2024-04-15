#!/usr/bin/env python

import sys
for k, v in sys.modules.items():
    print(k, v)

# accessing the name would fail
# print(contextlib)

# but the module has been imported and cached in sys.modules
contextlib = sys.modules["contextlib"] # same effect as "import contextlib"

print(contextlib)

