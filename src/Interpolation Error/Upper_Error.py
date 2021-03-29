import numpy as np
import math

def upper_error(x, f, neg=False):
    n = len(x)
    p = np.linspace(np.min(x), np.max(x))
    max_fun = 0
    max_prod = 0
    
    for val in p:
        fun = 0
        if neg:
            fun = abs(-f(val))
        else:
            fun = abs(f(val))

        if fun > max_fun:
            max_fun = fun

        res = np.array(list(map(lambda a: val - a, x)))
        prod = abs(np.prod(res))
        if prod > max_prod:
            max_prod = prod

    return (max_fun * max_prod) / math.factorial(n)