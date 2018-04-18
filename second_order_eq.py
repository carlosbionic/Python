import pylab

print ("Modelo de la ecuacion a*x^2 + b*x + c = 0")
a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
c = float(input("Valor de c: "))

#calculando el discriminante
delta = float(b**2-4*a*c)

if delta < 0:
    print("Ecuacion no tiene solucion real")

elif delta ==0:
    s = float(-b/2*a)
    print ("Solucion unica: ",s)

else:
    x1 = float((-b+((b**2 - 4*a*c))**0.5)/(2*a))
    x2 = float((-b-((b**2 - 4*a*c))**0.5)/(2*a))
    print("Las soluciones son las siguientes")
    print("X1: ",x1)
    print("X2: ",x2)

import matplotlib.pyplot as plt
import math
import numpy as np

# plot in separate window
#%matplotlib qt

x = np.arange(-10,10,0.5)
y = a*x**2 + b*x + c
plt.plot(x,y)
plt.title("a*x^2 + b*x + c = 0")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
