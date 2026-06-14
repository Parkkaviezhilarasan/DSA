def rmd(arr):
    res=[]
    for i in range(len(arr)):
        if arr[i] not in res:
            res.append(arr[i])
    return res
arr=[1,2,3,1,2,4]
print(rmd(arr))

def remd(arr):
    if not arr:
        return 0
    i=0
    for j in range(1,len(arr)):
        if arr[j]!=arr[i]:
            i+=1
            arr[i]=arr[j]
    return i+1
arr=[1,1,2,2,3,4]
k=remd(arr)
print(arr[:k])