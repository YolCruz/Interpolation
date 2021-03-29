import numpy as np

def neville(x, y, p):
    n = len(x) - 1
    i = 0
    j = 0
    step = 1
    first = True
    pij = np.ones((n+1,n+1))

    while True:
        if i == j:
            pij[i,i] = y[i]
        else:
            num = (p - x[j])*pij[i,j-1] - (p - x[i])*pij[i+1,j]
            den = x[i] - x[j]
            pij[i,j] = num / den
        
        i += 1
        j += step

        if j > n:
            if step + 1 > n:
                break
            else:
                if not first:
                    step += 1
                first = False
                i = 0
                j = step

    return pij[0,n]
