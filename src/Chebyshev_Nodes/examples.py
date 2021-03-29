#%%
from Chebyshev_Nodes import chebyshev_nodes, lagrange, graf, np
# %%
WID = 15
HEI = 10
#%% Example 1
# Evenly spaced nodes
f = lambda a: abs(a) + a/2 - a**2
#%%
x = np.linspace(-1, 1, 9)
y = f(x)
p = np.linspace(np.min(x), np.max(x),100)
#%%
pol = lagrange(x,y, p)
#%%
graf(p, f, pol, WID, HEI, save_path="../../images/Chebyshev nodes/Example1_chebyshev1.png")
#%%
# Chebyshev nodes
x = chebyshev_nodes(-1, 1, 9)
y = f(x)
p = np.linspace(np.min(x), np.max(x),100)
# %%
pol = lagrange(x,y, p)
# %%
graf(p, f, pol, WID, HEI, save_path="../../images/Chebyshev nodes/Example1_chebyshev2.png")
# %%
