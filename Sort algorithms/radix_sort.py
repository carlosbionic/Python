##################
### RADIX SORT ###
##################

import numpy as np
import time

def count_sort(v,dig): # Count sort according to digit 'dig' (1, 10, 100, ...)

		maxx = int(v[0]/dig)%10

		for i in range (len(v)):
			if (maxx <= int(v[i]/dig)%10):
				maxx = int(v[i]/dig)%10		# Find max of v	

		count = np.zeros(maxx+1,int)	

		for i in range (0,maxx+2):
			for j in range (len(v)):
				if (int(v[j]/dig)%10 == i): # Check the digit according to 'dig'
					count[i] += 1 # In count is the number of times number i appears

		# Now I store the sum of previous counts
		for i in range (1,len(count)):
			count[i] = count[i] + count[i-1]
		
		out = np.zeros(len(v),int)

		i = len(v)-1
		while (i>=0):
			out[count[int(v[i]/dig)%10]-1] = v[i]
			count[int(v[i]/dig)%10] = count[int(v[i]/dig)%10] - 1
			i -= 1

		print(out)
		return(out)

def radix_sort(v):
		# First, find the max of v, to know how many digits need to be sorted
		maxx = np.amax(v)
		n = len(str(abs(maxx))) # Count the digits of maxx

		for i in range(n):
			dig = 10**i
			print(dig)
			v = count_sort(v,dig)
	
		return(v)

a = 0
b = 10253
N = 200

# Generates a random array of N integer elements between a and b

arr = np.random.randint(a,b,N)

print(arr)

start_time = time.clock()
print( radix_sort(arr) )
print (time.clock() - start_time, "sec")
