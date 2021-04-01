## Examples

We'll use the next data points:

|       | | | | | | | | | | | | | | | | | 
|-------|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|**x :**|1|1|1|1|2|2|2|2|3|3|3|3|4|4|4|4|
|**y :**|1|2|3|4|1|2|3|4|1|2|3|4|1|2|3|4|
|**z :**|1|2|1|1|1|2|1|2|1|1|1|2|1|1|1|1|

With 50 evenly spaced points. First we import the interpolation funtions writen in Lagrange.py and Bilinear.py, and two plotting functions to see the results, defined in plotting.py. First we only use the points ```(1, 2, 3 ,4)``` for **x** and **y**  since these points are the only ones that are unique

```
from Bilinear import bilinear, np
from Lagrange import lagrange3D
from ploting import graf, anim

WID = 15
HEI = 10

x = np.array([1,2,3,4])
y = np.array([1,2,3,4])
z = np.array([[1,2,1,1], [1,2,1,2], [1,1,1,2], [1,1,1,1]])
n_points = 50
```

We need the combinations of **x** and **y** to obtain the points that are given to us, and we also need the points that are going to be evaluated in each algorithm and the combinations of those (this is done in order to make the graphs). To get these combinations we use Numpy's function ```meshgrid()```

```
vectx = np.linspace(np.amin(x), np.amax(x),n_points)
vecty = np.linspace(np.amin(y), np.amax(y),n_points)
Y1, X1 = np.meshgrid(x,y)
Y, X = np.meshgrid(vectx, vecty)
```

Calling X1 and Y1 

```
X1

array([[1, 1, 1, 1],
       [2, 2, 2, 2],
       [3, 3, 3, 3],
       [4, 4, 4, 4]])

Y1

array([[1, 2, 3, 4],
       [1, 2, 3, 4],
       [1, 2, 3, 4],
       [1, 2, 3, 4]])
```

We see that they now resemble the data given in the table, together with the vector **z** that we defined in the beginning. With these vectors we can apply both Bilinear and Lagrange interpolation and plot the results using the plotting functions

```
# Bilinear
Z = bilinear(x,y,z,vectx,vecty)

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

# --------------------------------------

# Lagrange
Z = lagrange3D(x,y,z, vectx, vecty)

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
```

The results are shown below:

<p float="center">
    <img src="../../images/Trilinear%20interpolation/Example1_bilinear.jpg" width="49%" />
    <img src="../../images/Trilinear%20interpolation/Example1_lagrange.jpg" width="49%" />
</p>

<p float="center">
    <img src="../../images/Trilinear%20interpolation/Example1_bilinear_animation.gif" width="49%" />
    <img src="../../images/Trilinear%20interpolation/Example1_lagrange_animation.gif" width="49%" />
</p>