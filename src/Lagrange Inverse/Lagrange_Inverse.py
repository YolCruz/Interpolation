import numpy as np
import matplotlib.pyplot as plt

def lagrange_inv(x, y, p):
    n = len(y)
    sum = 0
    for k in range(n):
        prod = product(y, p, k)
        sum += x[k] * prod
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

def graf(x, y, p, pol, WID, HEI, save=False, save_path=0):
    f = plt.figure()
    f.set_figwidth(WID)
    f.set_figheight(HEI)
    plt.plot(x,y,"o", label="$(x_i, y_i)$")
    plt.plot(p, pol, label="$P(x)$")
    plt.legend(loc="best", prop={'size': 16})
    plt.grid()
    if save:
        plt.savefig(save_path)
    else:
        plt.show()