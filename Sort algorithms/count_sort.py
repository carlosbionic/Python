################################
### COUNTING SORT ALGORITHM ###
################################

import numpy as np

def count_sort(v):

		maxx = v[0]
		minn = v[0]

		for i in range (len(v)):
			if (maxx <= v[i]):
				maxx = v[i]		# Find max of v
		#print(maxx)	

		for i in range (len(v)):
			if (minn >= v[i]):
				minn = v[i]		# Find min of v
		#print(minn)	

		#count = np.zeros(maxx-minn+1,int)	
		count = np.zeros(maxx+1,int)	
		#print(count)

		for i in range (0,maxx+2):
			#print(i)
			for j in range (len(v)):
				if (v[j] == i):
					count[i] += 1 # In count is the number of times number i appears
		#print (count)

		# Now I store the sum of previous counts
		for i in range (1,len(count)):
			count[i] = count[i] + count[i-1]
		
		#print(count)

		out = np.zeros(len(v))
		for i in range(len(v)):

			out[count[v[i]]-1] = v[i]
			count[v[i]] = count[v[i]] - 1
			#i -= 1

		return(out)

a = 0
b = 10
N = 70

# Generates a random array of N integer elements between a and b

arr = np.random.randint(a,b,N)
arr = list(arr) # Generates a list from an array

print(arr)
print( count_sort(arr) )
