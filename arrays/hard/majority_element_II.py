def majority_element(arr):
    d={}
    for num in arr:
        d[num]=d.get(num,0)+1
    for key in d:
        if d[key] > len(arr)//3:
            return key
print(majority_element([3,2,3]))