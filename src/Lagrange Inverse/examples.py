#%%
from Lagrange_Inverse import lagrange_inv, graf, np

WID = 15
HEI =10
# %%
# Example 1

x = np.array([0.0, 1.0, 1.5, 2.0])
y = np.array([2.5, 3.8, 4.6, 5.3])
# %%
p = np.linspace(np.min(y), np.max(y))
pol = lagrange_inv(x,y,p)
# %%
graf(y,x,p,pol,WID,HEI, save=True, save_path="../../images/Lagrange inverse/Example1_plot.png")
# %%
val = lagrange_inv(x,y, 2.75)
print(val) # 0.23257
# %%
