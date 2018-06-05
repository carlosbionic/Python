# Grafica una funcion lineal junto con el
# punto del grafico de la misma que esta
# mas cerca del (4,7)

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2,5,500)

plt.plot(x,3*x+5)
plt.scatter(4,7)
plt.scatter(1,8)

plt.axis('square')
plt.xlim(-3,7)
plt.ylim(3,12)
plt.show()
