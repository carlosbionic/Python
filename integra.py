import numpy as np
import scipy.integrate as int
import matplotlib.pyplot as plt

r=0
A=(1.-r)/2.
B=(1.+r)/2.

def f(x):
 if x > 1./3. and x< 2./3.:
     return A*np.cos(6.*np.pi*x)+B
 else:
     return 1

a=int.quad(f,0,1,epsabs=1e-5)
#b=int.quad(pow(f,2),0,1,epsabs=1e-5) 
#return a
#return b

print (a)
#print (b)
