def rearrange(arr):
    n=len(arr)
    pos_index=0
    neg_index=1
    ans=[0]*n
    for i in range(n):
        if arr[i]<0:
            ans[neg_index]=arr[i]
            neg_index+=2
        else:
            ans[pos_index]=arr[i]
            pos_index+=2
    return ans
arr = [1,2,-3,-4]
print(rearrange(arr))