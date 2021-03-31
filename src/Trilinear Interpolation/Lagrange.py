import numpy as np

def point_lagrange3D(x, y, z, pointX, pointY):
    n = len(x)
    m = len(y)
    s = 0
    for i in range(n):
        for j in range(m):
            L_x = product(x, pointX, i)
            L_y = product(y, pointY, j)
            s += z[i, j] * L_x * L_y
    return s

def lagrange3D(x, y, z, vectX, vectY):
    dimX, dimY = len(vectX), len(vectY)
    la = np.zeros((dimX, dimY))
    for indexX in range(dimX):
        for indexY in range(dimY):
            la[indexX, indexY] = point_lagrange3D(x, y, z, vectX[indexX], vectY[indexY])
    return la

def product(vec, p, i):
    n = len(vec)
    prod = 1
    for index in range(n):
        if index != i:
            num = p - vec[index]
            den = vec[i] - vec[index]
            prod *= num/den
    return prod