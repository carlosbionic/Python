import numpy as np
import matplotlib.pyplot as plt

def function_name(x):
    ff = (x**5 + 4*x**4 + 3*x**3 + 2*x**2 + x + 1)*np.exp(-x**2)
    return ff

x = np.linspace(-2, 2, 200)
y1 = function_name(x)

plt.grid(True)

y2 = (x**3)*np.exp(-x**2)

plt.plot(x,y1,'r',label="y1")
plt.plot(x,y2,'b',label="y2")

plt.xlabel('x')
plt.ylabel('y')

plt.legend()

plt.show()
