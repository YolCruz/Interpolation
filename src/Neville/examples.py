#%%
from Neville import *
# %%
# Example 1 Aproximate the  value 1/3 of the function 1/x
# with the given points
f = lambda x: 1/x

x = np.array([2,2.75,4])
y = np.array(f(x))
# %%
p = neville(x,y,3)
print(p) # 0.3295454545454546