import numpy as np


def u(x,y):
    e = np.e # readability
    return e**(-4*(x-0.5)**2 - 4*(y-0.5)**2)

def f(x,y):
    if x <= 1 and >= 0:
        if y <=1 and >=0:
            return 1
    else:
        return 0
    
# discretize
# decent visualization on 5th slide: https://www5.in.tum.de/lehre/vorlesungen/sci_comp/ws03/material/slides09.pdf

if __name__ == "__main__":
    print("abandon all hope, this is incomplete")
