# Преобразование Cython-код в C-код
# (файл setup.py)
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('run_cython.pyx'))