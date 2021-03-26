import numpy as np
from scipy.optimize import minimize as miny
import matplotlib.pyplot as plt


def f(x):
	return x**3 + 10*x**2 - 5*x - 7
xguess = 10


minimize = miny(f, xguess, method ='Powell')



y = np.arange(-20, 20, 0.01)


plt.figure()
plt.plot(y, f(y),label='f(x)',color = 'green')
plt.axvline(minimize.x, label = "min location %.2f"%(minimize.x) )
plt.legend()
plt.show()
print(minimize.x)



def g(x):
	return x**2 + 10*x - 12

minimize2 = miny(g, xguess, method = 'CG')
plt.figure()
plt.plot(y, g(y),label='g(x)',color = 'green')
plt.axvline(minimize2.x, label = "min location %.2f"%(minimize2.x) )
plt.legend()
plt.show()
print(minimize2.x)

