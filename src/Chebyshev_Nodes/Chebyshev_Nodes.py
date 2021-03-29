import numpy as np
import matplotlib.pyplot as plt

def chebyshev_nodes(x, y, n):
    new_x = np.zeros(n)

    for i in range(n):
        xk = np.cos((2*i + 1)*np.pi / (2*n))
        new_x[i] = (1/2)*(x + y) + (1/2)*(y - x)*xk

    return new_x

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

def graf(p, fun, pol, WID, HEI, save_path=0):
    g = plt.figure()
    g.set_figwidth(WID)
    g.set_figheight(HEI)
    plt.plot(p, fun(p), "r", label="$f(x)$")
    plt.plot(p, pol, label="$P(x)$")
    plt.legend(loc="best", prop={'size': 20})
    plt.grid()
    if save_path != 0:
        plt.savefig(save_path)
    else:
        plt.show()