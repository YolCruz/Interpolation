import numpy as np
import matplotlib.pyplot as plt

def lagrange(x, y, p):
    n = len(x)
    sum = 0
    for k in range(n):
        prod = product(x, p, k)
        sum += y[k] * prod
    return sum

def product(vec, p, i):
    n = len(vec)
    prod = 1
    for index in range(n):
        if index != i:
            num = p - vec[index]
            den = vec[i] - vec[index]
            prod *= num/den
    return prod

def graf(x, y, p, pol, WID, HEI):
    f = plt.figure()
    f.set_figwidth(WID)
    f.set_figheight(HEI)
    plt.plot(x,y,"o", label="$(x_i, y_i)$")
    plt.plot(p, pol, label="$P(x)$")
    plt.legend(loc="best")
    plt.grid()
    plt.show()