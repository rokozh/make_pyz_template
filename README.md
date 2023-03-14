# make_pyz_template
Template for make python pyz package
All python files placed in pyz archive are precompiled.
Data files can be stored in data subfolder
for access to data files add
import importlib.resources

read text files:
    str(importlib.resources.files("data").joinpath(name).read_bytes(), encoding='UTF8')
read binary files:
    importlib.resources.files("data").joinpath(name).read_bytes()

this access method is universal (inside pyz, pynstaller, plain)


# usage:
Place make_pyz/make_pyz.py in your project
Edit make_pyz.py (set application name, shebang line and needed files)
Place and edit "__main__.py" file (entry point)
If you need data files create data subfolder (keep empty "__init__.py" file)
