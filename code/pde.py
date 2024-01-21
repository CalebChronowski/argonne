# this is the 1d elliptical pde that we'll be exploring and using to generate data
import numpy as np

### definitions
def u(x):
    '''conductivity at point x in a 1D system'''
    return np.array(0.5) # throwaway value

def w(x):
    '''temp at point x in a 1D system'''
    return np.array(273.15) # throwaway value

def nabla(matrix):
    return np.gradient(matrix)

def eq1(x):
    '''returns the left hand side of equation 1 from the project kickoff document'''
    lhs = -1*nabla(np.e**(u(x))*nabla(w(x)))
    return lhs # left hand side of equation 1 on the project explanation document

if __name__ == "__main__":
    print(eq1(np.array([1])))