################################
### INSERTION SORT ALGORITHM ###
################################

import numpy as np


def ins_sort(v):

  n = len(v)

  if (n == 1):
    return v

  for i in range (1,n):

    j = i
    while (j >= 1):

      if (v[j-1] > v[j]): # Compare element i with element i+1
        v[j-1],v[j] = v[j],v[j-1] # Swap elements

      j-=1

  return v

a = -12.
b = 12.
N = 5

# Generates a random array of N elements between a and b

arr = np.random.rand(N)*(b-a) + a

arr=list(arr) # Generates a list from an array

print(arr)
print( ins_sort(arr) )
