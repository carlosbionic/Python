# QuickSort

def quickSort(arr):

    great = []
    less = []
    equal = []

    if len(arr) > 1:

        pivot = arr[-1] # Take last element of array as pivot

        for elem in arr:

            if elem > pivot:
                great += [elem]
            elif elem < pivot:
                less += [elem]
            elif elem == pivot:
                equal += [elem]

        return quickSort(less) + equal + quickSort(great)

    else:

        return arr

arr = [1, 5, 3, 11, 2, 3, 8]
print(quickSort(arr))
