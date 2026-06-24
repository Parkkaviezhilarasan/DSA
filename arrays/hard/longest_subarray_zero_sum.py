def subarr(arr):
    prefix_sum=0
    maxi=0
    mp={}
    for i in range(len(arr)):
        prefix_sum+=arr[i]
        if prefix_sum==0:
            maxi=i+1
        if prefix_sum in mp:
            maxi=max(maxi,i-mp[prefix_sum])
        else:
            mp[prefix_sum]=i
    return maxi
print(subarr([9, -3, 3, -1, 6, -5]))
