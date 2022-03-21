from  MonteCarlo import MonteCarlo
from math import pow

#s = MonteCarlo(100, -2, 2, -2, 2, 'x**3 + y**4 + 2 >= 0', '3*x + y**2 <= 2').get()
s = MonteCarlo(10**6, -2, 2, -2, 2, 'pow(x,3) + pow(y,4) + 2 >= 0', '3*x + pow(y,2) <= 2').get()
#s = MonteCarlo(10, -1, 1, -1, 1, '(x**2) + (y**2) < 1').get()
#s = MonteCarlo(10**6, -1, 1, -1, 1, 'pow(x,2) + pow(y,2) < 1').get()
print(s)