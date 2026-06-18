def leaders(arr):
    ans=[]
    current_max=arr[-1]
    ans.append(current_max)
    for i in range(len(arr)-2,-1,-1):
        if arr[i]>current_max:
            ans.append(arr[i])
            current_max=arr[i]
    return ans[::-1]
print(leaders([16,17,4,3,5,2]))