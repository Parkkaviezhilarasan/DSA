def insertion(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr          
arr=[12, 11, 13, 5, 6]
print(insertion(arr))

#with recursion
def insertion_1(arr,i,n):
    if i==n:
        return 
    j=i
    while j>0 and arr[j-1]>arr[j]:
        arr[j-1],arr[j]=arr[j],arr[j-1]
        j-=1
    insertion_1(arr, i+1, n)
arr=[12, 11, 13, 5, 6]  
insertion_1(arr, 1, len(arr))
print(arr)