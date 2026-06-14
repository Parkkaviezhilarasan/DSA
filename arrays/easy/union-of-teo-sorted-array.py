#brute force approach
def uni(arr1,arr2,n,m):
    freq={}
    for i in range(n):
        freq[arr1[i]]=freq.get(arr1[i],0)+1
    for i in range(m):
        freq[arr2[i]]=freq.get(arr2[i],0)+1
    union=sorted(freq.keys())
    return union
arr1=[1,2,4]
arr2=[1,3,4]
print(uni(arr1,arr2,3,3))

#brute force approach 2
def uni_b(arr1,arr2):
    st=set(arr1)|set(arr2)
    return sorted(st)
arr1=[1,2,4]
arr2=[1,3,4]
print(uni_b(arr1,arr2))

#optimal solution
def union(arr1,arr2):
    i=0
    j=0
    res=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            if not res or res[-1]!=arr1[i]:
                res.append(arr1[i])
            i+=1
        elif arr1[i]>arr2[j]:
            if not res or res[-1]!=arr2[j]:
                res.append(arr2[j])
            j+=1
        else:
            if not res or res[-1]!=arr1[i]:
                res.append(arr1[i])
            i+=1
            j+=1
    while i<len(arr1):
        if not res or res[-1]!=arr1[i]:
            res.append(arr1[i])
        i+=1
    while j<len(arr2):
        if not res or res[-1]!=arr2[j]:
            res.append(arr2[j])
        j+=1
    return res
arr1=[1,2,4]
arr2=[1,3,4]
print(union(arr1,arr2))