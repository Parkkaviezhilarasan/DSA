#brute force approach
def sortornot(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j]<arr[i]:
                return False
    return True
arr=[1,2,5,4,5]
arr1=[1,2,3,4,5]    
print("Brute force approach")
print("Array?", sortornot(arr))
print("Array1?", sortornot(arr1))

#optimal approach
def sortornot(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True
arr=[1,2,5,4,5]
arr1=[1,2,3,4,5]
print("Optimal approach")
print("Array?", sortornot(arr))
print("Array1?", sortornot(arr1))
