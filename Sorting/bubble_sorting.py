def bubble(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[64, 34, 25, 12, 22, 11, 90]
print(bubble(arr))

def bubble_1(arr, n):
    if n==1:
        return arr
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
    return bubble_1(arr, n-1)
arr=[64, 34, 25, 12, 22, 11, 90]
print(bubble_1(arr, len(arr)))