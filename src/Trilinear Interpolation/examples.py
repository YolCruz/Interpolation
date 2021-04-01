#%%
#from matplotlib import cm
from Bilinear import bilinear, np
from Lagrange import lagrange3D
from plotting import graf, anim
#%%
WID = 15
HEI = 10
# %%
x = np.array([1,2,3,4])
y = np.array([1,2,3,4])
z = np.array([[1,2,1,1], [1,2,1,2], [1,1,1,2], [1,1,1,1]])
n_points = 50
# %%
vectx = np.linspace(np.amin(x), np.amax(x),n_points)
vecty = np.linspace(np.amin(y), np.amax(y),n_points)
Y1, X1 = np.meshgrid(x,y)
Y, X = np.meshgrid(vectx, vecty)
#%%
# Bilinear
Z = bilinear(x,y,z,vectx,vecty)
# %%
sp="../../images/Trilinear interpolation/Example1_bilinear.jpg"
graf(
    X1, Y1, z, 
    X, Y, Z, 
    WID, HEI, 
    title="Bilinear", 
    save_path=sp, 
    font_size=20.0, 
    pad=20.0, 
    ty=1
)
#%%
sp_a="../../images/Trilinear interpolation/Example1_bilinear_animation.gif"

anim(
    X1, Y1, z, 
    X, Y, Z, 
    WID, HEI, 
    frames=200, 
    title="Bilinear", 
    save_path=sp_a, 
    interval=50, 
    font_size=20.0, 
    pad=20.0, 
    ty=1
)
#%%
# --------------------------------------

# Lagrange
Z = lagrange3D(x,y,z, vectx, vecty)
#%%
sp="../../images/Trilinear interpolation/Example1_lagrange.jpg"

graf(
    X1, Y1, z, 
    X, Y, Z, 
    WID, HEI, 
    title="Lagrange", 
    save_path=sp, 
    font_size=20.0, 
    pad=20.0, 
    ty=1
)
#%%
sp_a="../../images/Trilinear interpolation/Example1_lagrange_animation.gif"

anim(
    X1, Y1, z, 
    X, Y, Z, 
    WID, HEI, 
    frames=300, 
    title="Lagrange", 
    save_path=sp_a, 
    interval=50, 
    font_size=20.0, 
    pad=20.0, 
    ty=1
)
