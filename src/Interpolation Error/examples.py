#%%
from Upper_Error import *
# %%
# Ejemplo 1
x = np.linspace(0,1,10)
# %%
err = upper_error(x, np.sin, neg=True)
#print(mf, mp)
print(err)

#%%
# Ejemplo 2
x = np.linspace(-1, 1, 5)
# %%
err = upper_error(x,np.exp)
print(err)
# %%
