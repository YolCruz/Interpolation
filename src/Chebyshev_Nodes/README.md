## Example

For the example, we will consider the function 

![function](../../images/Chebyshev%20nodes/function.png)

We'll do the Lagrange interpolation using nine evenly spaced nodes to compare with the interpolation using Chebyshev nodes.

### Evenly spaced nodes

Using evenly spaced nodes

```
from Chebyshev_Nodes import chebyshev_nodes, lagrange, graf, np

WID = 15
HEI = 10

f = lambda a: abs(a) + a/2 - a**2

x = np.linspace(-1, 1, 9)
y = f(x)
p = np.linspace(np.min(x), np.max(x),100)

pol = lagrange(x,y, p)

graf(p, f, pol, WID, HEI)
```

The helper function ```graf()``` -defined in the Chebyshev_Nodes.py file- will produce the next image:

![Even nodes](../../images/Chebyshev%20nodes/Example1_chebyshev1.png)

We can see that the interpolation is not the best. This happens when the points in the vector x is very large -degree of x-, as in this case, we have 9 points. 

### Chebyshev nodes

Using Chebyshev nodes instead of evenly spaced ones we get:

```
x = chebyshev_nodes(-1, 1, 9)
y = f(x)
p = np.linspace(np.min(x), np.max(x),100)

pol = lagrange(x,y, p)

graf(p, f, pol, WID, HEI)
```

![Chebyshev nodes](../../images/Chebyshev%20nodes/Example1_chebyshev2.png)

This is a much better result as it approximates most parts of the function and has less fluctuations.