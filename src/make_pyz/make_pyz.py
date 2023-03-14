#!/usr/bin/python3.10

"""
PYZ maker template
(C) Roman Kozhemiakin 2023


subfolder data - used for files requried by application
for access to data files add
import importlib.resources

read text files:
    str(importlib.resources.files("data").joinpath(name).read_bytes(), encoding='UTF8')
read binary files:
    importlib.resources.files("data").joinpath(name).read_bytes()

this access method is universal (inside pyz, pynstaller, plain)
"""

import os
import zipfile
from pathlib import Path
import py_compile as pyc

# Place name of App (result AppName.pyz)
app_name = 'AppName'

# Place shebang line include desired python version
shebang = b'#!/usr/bin/python3.10\x0A'

pyz = Path(f'{app_name}.pyz').resolve()
os.chdir('..')

# Place list of src files
src = list(Path('./').glob('*.py')) + list(Path('./data').glob('*.*'))

with zipfile.ZipFile(pyz, 'w') as _zip:
    for i in src:
        if i.suffix == '.py':
            pyc.compile(i, 'temp.pyc')
            _zip.write('temp.pyc', i.with_suffix('.pyc'))
        else:
            _zip.write(i)
os.remove('temp.pyc')
pyz.write_bytes(shebang + pyz.read_bytes())
