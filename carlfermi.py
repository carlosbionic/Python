import numpy as np
import scipy.integrate as int
import matplotlib.pyplot as plt

r=0.
A=(1.-r)/2.
B=(1.+r)/2.
def carlos(q):
    #c=1./((1.-q)*np.log(3.))
    def f(x):
        if x >= 1/2. and x < 2/3.:
	    return (1.-r)/(1.+np.exp(-120.*(x-0.63))) + r
        elif x > 1/3. and x < 1/2.:
            return (1.-r)/(1.+np.exp(-120.*((1.-x)-0.63))) + r
        else:
            return 1
    def arriba(x):
        return np.power(f(x),q)
    
 
    def abajo(q):
        return np.power(int.quad(f,0,1,epsabs=1e-10),q)
    
    h=np.log(int.quad(arriba,0,1,epsabs=1e-10)/abajo(q))/((1.-q)*np.log(3.))+1.
    return h
    
    
qvect=np.arange(0,11,.01)
d=np.zeros(np.size(qvect))
d[100]=1.76
file=open('dimensionfitteo.dat','w')
for t in range(np.size(qvect)):
    if qvect[t]!=1:
        d[t]=carlos(qvect[t])[0]+1
        print>>file, qvect[t],d[t]
        
file.close()
plt.plot(qvect,d)
plt.show()      
