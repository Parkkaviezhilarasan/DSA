#brute force approach
def zero(arr):
    ans=[0]*len(arr)
    j=0
    for i in range(len(arr)):
        if arr[i]!=0:
            ans[j]=arr[i]
            j+=1
    return ans
arr=[0,1,0,3,12]
print(zero(arr))

#brute  force approach 2
def zero_b(arr):
    count=0
    ans=[]
    for i in range(len(arr)):
        if arr[i]==0:
            count+=1
        else:
            ans.append(arr[i])
    for i in range(count):
        ans.append(0)
    return ans
arr=[0,1,0,3,12]
print(zero_b(arr))

#optimal solution
def zero_1(arr):
    j=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[j],arr[i]=arr[i],arr[j]
            j+=1
    return arr
arr=[0,1,0,3,12]
print(zero_1(arr))