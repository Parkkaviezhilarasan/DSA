def linear(arr,n):
    for i in range(len(arr)):
        if arr[i]==n:
            return i
    return -1
arr=[1,2,3,4,5]
print(linear(arr,3))