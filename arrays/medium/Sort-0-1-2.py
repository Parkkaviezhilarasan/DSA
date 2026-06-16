def szot(arr):
    c0=0
    c1=0
    c2=0
    for i in range(len(arr)):
        if arr[i]==0:
            c0+=1
        elif arr[i]==1:
            c1+=1
        else:
            c2+=1
    return c0*[0]+c1*[1]+c2*[2]
test_arr = [2, 0, 2, 1, 1, 0]
print(szot(test_arr))