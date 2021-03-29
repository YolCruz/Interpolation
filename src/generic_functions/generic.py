import numpy as np
import matplotlib.pyplot as plt

def graf(x, y, p, pol, WID, HEI):
    f = plt.figure()
    f.set_figwidth(WID)
    f.set_figheight(HEI)
    plt.plot(x,y,"o", label="$(x_i, y_i)$")
    plt.plot(p, pol, label="$P(x)$")
    plt.legend(loc="best", prop={'size': 20})
    plt.grid()
    plt.show()

def Ruffini(a, p):
    n = len(a) - 1
    b = a[n]
    for i in range(n-1, -1, -1):
        b = a[i] + p*b

    return b