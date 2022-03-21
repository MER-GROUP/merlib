# метод Монте-Карло
# S = (k/n) * So

# импорт модуля random
# uniform() - возвращает случайное число с плавающей точкой, 
# но при этом она позволяет задавать диапазон для 
# отбора значений от а до б включительно
from random import uniform

cdef class MonteCarlo:
    cdef double x1, x2, x, y1, y2, y, So
    cdef list s
    cdef int n, output, k

    def __cinit__(self, n, x1, x2, y1, y2, *s, output = False):
        self.n = n
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.s = [*s]
        self.output = output
        self.So = (abs(self.x1) + abs(self.x2)) * (abs(self.y1) + abs(self.y2))
        self.k = int()

    cpdef get(self):
        cdef int i
        cdef list arr
        cdef double k, n, So
        while True:
            try:
                for _ in range(self.n):
                    self.x = uniform(self.x1, self.x2)
                    self.y = uniform(self.y1, self.y2)
                    arr = list(self.s.copy())

                    for i in range(len(arr)):
                        arr[i] = arr[i].replace('x', str(self.x))
                        arr[i] = arr[i].replace('y', str(self.y))
                        arr[i] = eval(arr[i])
                    if all([i for i in arr]):
                        self.k += 1
                k, n, So = self.k, self.n, self.So
                print('k =', k)###
                print('n =', n)###
                print('So =', So)###
                return (k / n) * So
            except ZeroDivisionError:
                continue

'''      
if __name__ == '__main__':
    s = MonteCarlo(10**6, -2, 2, -2, 2, 'x**3 + y**4 + 2 >= 0', '3*x + y**2 <= 2').get()
    print(s)
# n = 10**6       # количество испытаний
'''