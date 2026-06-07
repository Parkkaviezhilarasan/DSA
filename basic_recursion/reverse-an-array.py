def reverse(arr,i):
    n=len(arr)
    if i>=n//2:
        return
    arr[i],arr[n-1-i]=arr[n-1-i],arr[i]
    reverse(arr,i+1)
arr=[1,2,3,4,5]
reverse(arr,0)
print(arr)