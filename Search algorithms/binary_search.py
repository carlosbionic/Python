#####################
### BINARY SEARCH ###
#####################

def binary_search (array,elem,l,r):

		if (r >= l):

			med = int((l + r)/2) # Middle between l and r

			if ( elem == array[med]):
				return med

			elif ( elem > array[med] ):
				return binary_search (array,elem,med+1,r) # Take 2nd half

			else:
				return binary_search (array,elem,l,med-1) # Take 1st half

		else:
			return -1

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
x = 5
pos = binary_search (arr,x,0,len(arr)-1)

if (pos == -1):
	print('Element',x,'is not present')
else:
	print('Element',x, 'is at position',pos)
