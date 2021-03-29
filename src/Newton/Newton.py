import numpy as np
import matplotlib.pyplot as plt

def newton_coefs(x,y):
    n = len(x)
    coefs = np.copy(y)

    for index in range(1, n):
        fs = np.ones(n)
        for f in range(index, n):
            num = coefs[f] - coefs[f-1]
            den = x[f] - x[f-index]
            fs[f] = num/den

        for i in range(index, n):
            coefs[i] = fs[i]
    
    return coefs

def newton_compact(coefs, x, p):
    n = len(x) - 1
    products = coefs[n]
    for index in range(n,0,-1):
        products = (p - x[index-1])*products + coefs[index-1]
    
    return products

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