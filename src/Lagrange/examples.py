#%%
from Lagrange import lagrange, graf, np

WID = 15
HEI =10
# Example 1. 2 Interpolate x^2
#%%
x = np.array([1,2,3])
y = np.array([1,4,9])
# %%
p = np.linspace(np.min(x), np.max(x))
pol = lagrange(x,y,p)
# %%
graf(x,y,p,pol,WID,HEI)

# %%
# Example 2 Interpolate x^3
x = np.array([1,2,3,4])
y = np.array([1,8,27,64])
# %%
p = np.linspace(np.min(x), np.max(x))
pol = lagrange(x,y,p)
# %%
graf(x,y,p,pol,WID,HEI)
# %%
# Example 3 Determine f(7)
x = np.array([1,2,3,4,5,6])
y = np.array([1,1,2,3,5,8])
# %%
p = np.linspace(np.min(x), np.max(x))
pol = lagrange(x,y,p)
# %%
graf(x,y,p,pol,WID,HEI)
# %%
val = lagrange(x,y,7)
print(val)