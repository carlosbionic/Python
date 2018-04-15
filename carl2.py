import numpy as np
import scipy.integrate as int
import matplotlib.pyplot as plt

r=0
A=(1.-r)/2.
B=(1.+r)/2.
def carlos(q):
    c=1./((1.-q)*np.log(3.))
    def f(x):
        if x > 1/3. and x< 2/3.:
            return A*np.cos(6.*np.pi*x)+B
        else:
            return 1
    def arriba(x):
        return f(x)**q
    
 
    def abajo(q):
        return np.power(int.quad(f,0,1,epsabs=1e-12),q)
    
    h=c*np.log(int.quad(arriba,0,1,epsabs=1e-12)/abajo(q))+1.
    return h
    
    
qvect=np.arange(0,11,.01)
d=np.zeros(np.size(qvect))
d[100]=1.9
file=open('dimensionfitteo.dat','w')
for t in range(np.size(qvect)):
    if qvect[t]!=1:
        d[t]=carlos(qvect[t])[0]+1
        print>>file, qvect[t],d[t]
        
file.close()
plt.plot(qvect,d)
plt.show()      
