################################
### SELECTION SORT ALGORITHM ###
################################

import numpy as np

def sel_sort(v):

		for j in range (0,len(v)-1):
			aux = v[j]
			k = j

			for i in range (j+1,len(v)):
				if (v[i]<aux):
					aux = v[i]
					k = i # Save minimum to aux (the position)

			v[j],v[k] = v[k],v[j]

			print(v)
		return(v)

a = -12.
b = 12.
N = 5

# Generates a random array of N elements between a and b

arr = np.random.rand(N)*(b-a) + a

arr=list(arr) # Generates a list from an array

print(arr)
print( sel_sort(arr) )
