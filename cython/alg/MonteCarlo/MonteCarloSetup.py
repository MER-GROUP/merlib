# Преобразование Cython-код в C-код
# python MonteCarloSetup.py build_ext --inplace
from distutils.core import setup
from Cython.Build import cythonize

setup(name='MonteCarlo',
      ext_modules=cythonize("MonteCarlo.pyx"))