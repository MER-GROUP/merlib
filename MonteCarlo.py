# метод Монте-Карло
# S = (k/n) * So
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
                return (self.k / self.n) * self.So
            except ZeroDivisionError:
                continue
        
if __name__ == '__main__':
    s = MonteCarlo(10**4, -2, 2, -2, 2, 'x**3 + y**4 + 2 >= 0', '3*x + y**2 <= 2').get()
    print(s)

# n = 10**6       # количество испытаний