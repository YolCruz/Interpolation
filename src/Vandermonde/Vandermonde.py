import numpy as np

def different(x):
    n = len(x)
    unique = np.unique(x)
    if len(unique) == n:
        return True
    return False

def vandermonde_matrix(x):
    if not different(x):
        print("The values of x must not repeat!")
        return
    n = len(x)
    V = np.ones([n,n])
    for i in range(1,n):
        V[:,i] = V[:, i-1] * x
    return V

def vandermonde(x,y):
    v = vandermonde_matrix(x)
    a = np.linalg.solve(v,y)

    return a

def Ruffini(a, p):
    n = len(a) - 1
    b = a[n]
    for i in range(n-1, -1, -1):
        b = a[i] + p*b

    return b