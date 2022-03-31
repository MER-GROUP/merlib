# Преобразование Cython-код в C-код
# (файл factorial_setup.py)
# python factorial_setup.py build_ext --inplace
from distutils.core import setup
from Cython.Build import cythonize

setup(name='cython_test_factorial',
      ext_modules=cythonize("cython_test_factorial.pyx"))