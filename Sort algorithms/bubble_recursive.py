def bubble(arr,n):
    if (n==1): # If arr has 1 element, return arr as it is
      return

    swap = False
    for i in range(n-1):
      if (arr[i] > arr[i+1]):
        arr[i],arr[i+1] = arr[i+1],arr[i] # Swaps elements
        swap = True
    if (swap == True):
      bubble(arr,n-1) # If swapped, call bubble again
    else:
      return # If not swapped, then arr is already sorted

v=[1,3,1,2,2,0,1,-3,-2,7,6]
print(v)

bubble(v,len(v))

print(v)
