#selection sort.
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr
#input.
arr=[8,3,4,5,2,9,1]
print("The orginal array:",arr)
selection_sort(arr)
print("The sorted array:",arr)
