#brute force approach
def largest(arr):
    arr.sort()
    return arr[-1]
arr = [10, 2, 8, 5]
print(largest(arr))

#optimal approach
def largest(arr):
    max_ele=arr[0]
    for i in range(len(arr)):
        if arr[i]>max_ele:
            max_ele=arr[i]
    return max_ele
arr = [10, 2, 8, 5]
print(largest(arr))
