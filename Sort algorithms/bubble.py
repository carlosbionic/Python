import numpy as np

a = -12.
b = 12.
N = 4

# Generates a random array of N elements between a and b

v = np.random.rand(N)*(b-a) + a
#print (v)

# Bubble sort (ascending order)

while(True):
  count = 0
  print (v) 

  for i in range(N-1): # Starts with 0 to N-1
    
    if (v[i+1]<v[i]):
      v[i], v[i+1] = v[i+1], v[i]
      count += 1

  if (count == 0): 
    break
