# метод Монте-Карло
# S = (k/n) * So

# импорт модуля random
# uniform() - возвращает случайное число с плавающей точкой, 
# но при этом она позволяет задавать диапазон для 
# отбора значений от а до б включительно
from random import uniform

#from __future__ import print_function

cdef class MonteCarlo:
    cdef double n, x1, x2, y1, y2
    cdef list s

    def __cinit__(self, n, x1, x2, y1, y2, *s, output = False):
        self.n = n
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.s = [*s]

    cpdef describe(self):
        #print("hello", uniform(5, 7))
        #return uniform(5, 7)
        return self.s


'''
from random import uniform

class MonteCarlo:
    def __init__(self, n, x1, x2, y1, y2, *s, output = False):
        self.So = (abs(x1) + abs(x2)) * (abs(y1) + abs(y2))
        # print(self.So)
        self.x = int()
        self.x1 = x1
        self.x2 = x2
        self.y = int()
        self.y1 = y1
        self.y2 = y2
        self.n = n
        self.k = int()
        self.s = [*s]
        # print(s)
        # arr = list(self.s)
        # print(arr)
        
    def get(self):
        step = int(1)
        while True:
            try:
                for _ in range(self.n):
                    self.x = uniform(self.x1, self.x2)
                    self.y = uniform(self.y1, self.y2)
                    arr = list(self.s.copy())
                    for i in range(len(arr)):
                        arr[i] = arr[i].replace('x', str(self.x))
                        arr[i] = arr[i].replace('y', str(self.y))
                        # print(arr[i])
                        arr[i] = eval(arr[i])
                        # print(arr[i])
                    if all(i for i in arr):
                        self.k += 1
                    print(step)###
                    step += 1###
                return (self.k / self.n) * self.So
            except ZeroDivisionError:
                continue
        
if __name__ == '__main__':
    s = MonteCarlo(10**6, -2, 2, -2, 2, 'x**3 + y**4 + 2 >= 0', '3*x + y**2 <= 2').get()
    print(s)

# n = 10**6       # количество испытаний
'''