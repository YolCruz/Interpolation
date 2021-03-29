#%%
import matplotlib.pyplot as plt
from Vandermonde import vandermonde, Ruffini, np
#%%
WID = 15
HEI =10
#%% Funciones conocidas 
# Ejemplo 1
x = np.array([0, 1, 3, 6])
y = np.array([-3, 0, 5, 7])
# %%
coefs = vandermonde(x,y)
t = np.linspace(np.min(x), np.max(x))
pt = Ruffini(coefs, t)
# %%
f = plt.figure()
f.set_figwidth(WID)
f.set_figheight(HEI)
plt.plot(x,y,"o", label="$(x_i, y_i)$")
plt.plot(t, pt, label="$P(x)$")
plt.legend(loc="best")
plt.grid()
plt.show()
# %%
# Aproximar el valor de f(x) para x = 1.8
val = Ruffini(coefs, 1.8)
print(val)
# %%
# Ejemplo 2
# Aproximar la función f(x) = (2/x)^{1/2}*sin(x) en el intervalo [1, pi] con
# 4 nodos igualmente espaciados
f = lambda x: (2/x)**(1/2) * np.sin(x)

x = np.linspace(1, np.pi, 4)
y = f(x)
# %%
coefs = vandermonde(x,y)
t = np.linspace(np.min(x), np.max(x))
pt = Ruffini(coefs, t)
# %%
f = plt.figure()
f.set_figwidth(WID)
f.set_figheight(HEI)
plt.plot(x,y,"o", label="$(x_i, y_i)$")
plt.plot(t, pt, label="$P(x)$")
plt.legend(loc="best")
plt.grid()
plt.show()
# %%
coefs = vandermonde(x,y)
t = np.linspace(np.min(x), np.max(x))
pt = Ruffini(coefs, t)