#Binary search.
def binary_search(arr,key):
    low=0
    high=len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid]== key:
            return mid
        elif arr[mid]<key:
            low=mid+1
        else:
            low=mid-1
#Taking input
n=int(input("Enter a number of elements:"))
arr=[]
print("Enter a elements:")
for i in range(n):
    arr.append(int(input()))
key=int(input("Enter a elements to search:"))
result=binary_search(arr,key)
if result !=-1:
    print("Elements found at index",result)
else:
    print("Elements not found")

