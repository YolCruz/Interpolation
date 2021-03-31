import numpy as np

def point_bilinear(x,y,z, pointX, pointY):
    i = index_vec(x, pointX)
    j = index_vec(y, pointY)

    l_ij = (x[i] - pointX)*(y[j] - pointY)
    l_i1j1 = (x[i+1] - pointX)*(y[j+1] - pointY)
    l_i1j = (x[i+1] - pointX)*(y[j] - pointY)
    l_ij1 = (x[i] - pointX)*(y[j+1] - pointY)

    z_ij = z[i,j]
    z_i1j1 = z[i+1,j+1]
    z_i1j = z[i+1,j]
    z_ij1 = z[i, j+1]

    num_1 = l_ij*z_i1j1 + l_i1j1*z_ij
    num_2 = l_i1j*z_ij1 + l_ij1*z_i1j
    den = (x[i+1] - x[i]) * (y[j+1] - y[j])

    return (num_1 - num_2) / den

def bilinear(x, y, z, vectX, vectY):
    dimX, dimY = len(vectX), len(vectY)
    bi = np.zeros((dimX, dimY))
    for indexX in range(dimX):
        for indexY in range(dimY):
            bi[indexX, indexY] = point_bilinear(x, y, z, vectX[indexX], vectY[indexY])

    return bi

def index_vec(vec, point):
    n = len(vec) - 1
    if point < vec[0]:
        return 0
    elif point > vec[n]:
        return n-2
    else:
        for i in range(n):
            if vec[i] <= point and point <= vec[i+1]:
                return i

#def graf()