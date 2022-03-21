from MonteCarlo import MonteCarlo
from math import pow

#print(mc.__doc__)
print(MonteCarlo.__doc__)
#s = MonteCarlo(100, -2, 2, -2, 2, 'x**3 + y**4 + 2 >= 0', '3*x + y**2 <= 2').get()
MonteCarlo(10**5, -2, 2, -2, 2, 'pow(x,3) + pow(y,4) + 2 >= 0', '3*x + pow(y,2) <= 2')
MonteCarlo(10**5, -2, 2, -2, 2, 'pow(x,3) + pow(y,4) + 2 >= 0', '3*x + pow(y,2) <= 2',output=True)
s = mc(10**5, -2, 2, -2, 2, 'pow(x,3) + pow(y,4) + 2 >= 0', '3*x + pow(y,2) <= 2').get()
print(s)
#s = MonteCarlo(10, -1, 1, -1, 1, '(x**2) + (y**2) < 1').get()
s = MonteCarlo(10**5, -1, 1, -1, 1, 'pow(x,2) + pow(y,2) < 1').get()
print(s)