#Bruteforce approach
def numbers(arr):
    for i in range(len(arr)):
        count=0
        for j in range(len(arr)):
            if arr[i]==arr[j]:
                count+=1
        if count==1:
            return arr[i]
arr=[1,2,3,2,1]
print(numbers(arr))

#optimal approach
def nummbers(arr):
    xor=0
    for i in range(len(arr)):
        xor^=arr[i]
    return xor
arr=[1,2,3,2,1]
print(nummbers(arr))