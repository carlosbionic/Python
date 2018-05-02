#####################
### LINEAR SEARCH ###
#####################

def linear_search (arr,elem):
		
		n = len(arr)
		count = 0
		
		for i in range(n):
			if (arr[i] == elem):
				print ('Element ', elem,'is in position ',i)
				count = 1

		if (count == 0):
			print ('Element ', elem,'is not present in ',arr)

v = [10,20,80,30,60,50,110,100,130,170]
linear_search(v,170)
