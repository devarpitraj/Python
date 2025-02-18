from scipy.optimize import root, minimize
import numpy as np

# finding root
def eqn(x):
    return x + np.cos(x)

myroot = root(eqn, 0)
print(myroot.x)
print(myroot)

# finding minima
def eqn1(x):
    return x**2 + x + 2

mymin = minimize(eqn1, 0, method='L-BFGS-B')
print(mymin.x)
print(mymin)