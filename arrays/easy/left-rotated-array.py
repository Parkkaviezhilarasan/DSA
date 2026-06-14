def leftrotate(arr):
    n=len(arr)
    res=[0]*n
    for i in range(1,n):
        res[i-1]=arr[i]
    res[n-1]=arr[0]
    return res
arr=[1,2,3,4,5]
print(leftrotate(arr))

#optimal solution
def leftrotate_1(arr):
    n=len(arr)
    temp=arr[0]
    for i in range(1,n):
        arr[i-1]=arr[i]
    arr[n-1]=temp
    return arr
arr=[1,2,3,4,5]
print(leftrotate_1(arr))    
