#%%
from Newton import *

WID = 15
HEI =10
# %% Newton Coefficients
# Example 1 
x = np.array([-3/2, -3/4, 0, 3/4, 3/2])
y = np.array([-14.1014, -0.931596, 0, 0.931596, 14.1014])
# %%
c = newton_coefs(x, y)
print(c)
# %% Newton Interpolation
# Example 2
x = np.array([1,2,3,4])
y = np.array([6,9,2,5])
# %%
c = newton_coefs(x, y)
print(c)
# %%
p = np.linspace(np.min(x), np.max(x))
pol = newton_compact(c, x, p)
# %%
graf(x,y,p,pol, WID, HEI, save=True, save_path="../../images/Newton/Example1_Newton.png")
# %%
