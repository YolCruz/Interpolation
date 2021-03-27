The example 1 is from Dr's Anita Pal [Numerical Analysis](http://epgp.inflibnet.ac.in/epgpdata/uploads/epgp_content/S000025MS/P001476/M014250/ET/1456308981E-textofChapter2Module6.pdf). 
We are given a table with time and velocity of a particle moving with non-uniform velocity, as follows:

<center>

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| t:  | 0.0 | 1.0 | 1.5 | 2.0 |
| v:  | 2.5 | 3.0 | 4.6 | 5.3 |

</center>

And we are asked to use this table to determine the time when the velocity of the particle becomes 2.75

First we do the necessary imports and set the width and height of the chart for later:

```
import numpy as np
from Lagrange_Inverse import lagrange_inv, graf

WID = 15
HEI =10
```

In this problem, our variable *x* is the time and *y* is the velocity
```
x = np.array([0.0, 1.0, 1.5, 2.0])
y = np.array([2.5, 3.8, 4.6, 5.3])
```

Now we need to declare the points that are going to be evaluated in the function. These are the points that appear as *y* in the formula:

<center>

![Inverse Lagrange interpolation](../../images/Lagrange%20inverse/Lag_inv.png)

</center>

We can easily declare them as all the points between the minimum and maximum values of our array of velocity:

```
p = np.linspace(np.min(y), np.max(y))
```

Now we do the interpolation with this points

```
pol = lagrange_inv(x,y,p)
```

and plot the results:

```
graf(y,x,p,pol,WID,HEI)
```

<center>

![Inverse Lagrange interpolation](../../images/Lagrange%20inverse/Example1_plot.png)

</center>

to determine the time, we call the function ```lagrange_inv()``` with the point 2.75, as shown:

```
val = lagrange_inv(x,y, 2.75)
print(val)
```
The code above will print **0.23257**, the solution we wanted.