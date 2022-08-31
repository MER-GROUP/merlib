# Преобразование Cython-код в C-код
# python BogoSortSetup.py build_ext --inplace
from distutils.core import setup
from Cython.Build import cythonize

setup(name='BogoSort',
      ext_modules=cythonize("BogoSort.pyx"))