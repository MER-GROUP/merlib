# импорт модуля python_test_factorial
import python_test_factorial
# импорт модуля cython_test_factorial
import cython_test_factorial
# импорт модуля time
import time

# число для факториала
number = 100000

# факториал python
start = time.time()
python_test_factorial.test(number)
end =  time.time()

# время вычисления факториала python
py_time = end - start
print("Python time = {}".format(py_time))

# факториал cython
start = time.time()
cython_test_factorial.test(number)
end =  time.time()

# время вычисления факториала cython
cy_time = end - start
print("Cython time = {}".format(cy_time))

# разница времени вычисления факториала python и cython
print("Speedup = {}".format(py_time / cy_time))