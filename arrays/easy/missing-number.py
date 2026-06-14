#brute force approach
def miss(arr):
    for i in range(len(arr)):
        if arr[i]!=i+1:
            return False
    return True
arr=[1,2,3,4,5]
print(miss(arr))

#brute force approach2
def miss1(arr):
    total_sum=sum(arr)
    n=len(arr)+1
    expected_sum=(n*(n+1))//2
    return expected_sum-total_sum
arr=[1,2,3,5]
print(miss1(arr))

#optimal solution
def miss2(arr):
    n=len(arr)+1
    xor1=0
    xor2=0
    for i in range(n-1):
        xor1^=arr[i]
    for i in range(1,n+1):
        xor2^=i
    return xor1^xor2
arr=[1,2,3,5]
print(miss2(arr))
