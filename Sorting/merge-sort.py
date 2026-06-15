def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid=len(arr)//2
    left=[]
    for i in range(0,mid):
        left.append(arr[i])
    right=[]
    for i in range(mid,len(arr)):
        right.append(arr[i])
    left=merge_sort(left)
    right=merge_sort(right)
    return merge(left,right)
def merge(left,right):
    res=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    while i <len(left):
        res.append(left[i])
        i+=1
    while j<len(right):
        res.append(right[j])
        j+=1
    return res
arr=[38, 27, 43, 3, 9, 82,10]
print(merge_sort(arr))      