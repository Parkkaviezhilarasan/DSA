#brute force approach
def twosumm(arr,tar):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == tar:
                return [i,j]
arr = [2,7,11,15]
tar = 9
print(twosumm(arr,tar))

#optimal approach 
def twosum(arr,tar):
    d = {}
    for i in range(len(arr)):
        c=tar-arr[i]
        if c in d:
            return [d[c],i]
        else:
            d[arr[i]]=i
arr = [2,7,11,15]
tar = 9
print(twosum(arr,tar))

#optimal approach with sorted array
def twosum_sorted(arr,tar):
    left = 0
    right = len(arr)-1

    while left < right:
        s = arr[left]+arr[right]
        if s == tar:
            return [left,right]
        elif s < tar:
            left += 1
        else:
            right -= 1

arr = [2,7,11,15]
tar = 9
print(twosum_sorted(arr,tar))