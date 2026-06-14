#brute forcee
def smlr(arr):
    arr.sort()
    return arr[1],arr[-2]
arr = [10, 2, 8, 5]
print("Brute force approach:", smlr(arr))

#better approach
def smlr(arr):
    max_ele=arr[0]
    min_ele=arr[0]
    for i in range(len(arr)):
        if arr[i]>max_ele:
            max_ele=arr[i]
        if arr[i]<min_ele:
            min_ele=arr[i]
    second_smallest=float('inf')
    second_largest=float('-inf')
    for i in range(len(arr)):
        if arr[i]!=max_ele and arr[i]>second_largest:
            second_largest=arr[i]
        if arr[i]!=min_ele and arr[i]<second_smallest:
            second_smallest=arr[i]
    return second_smallest,second_largest
arr = [10, 2, 8, 5]
print("Better approach:", smlr(arr))

#optimal approach
class solution:
    def small(arr):
        n=len(arr)
        if n<2:
            return -1
        sm=float('inf')
        ssm=float('inf')
        for i in range(n):
            if arr[i]<sm:
                ssm=sm
                sm=arr[i]
            elif arr[i]!=sm and arr[i]<ssm:
                ssm=arr[i]
        return ssm
    def large(arr):
        n=len(arr)
        if n<2:
            return -1
        lg=float('-inf')
        slg=float('-inf')
        for i in range(n):
            if arr[i]>lg:
                slg=lg
                lg=arr[i]
            elif arr[i]!=lg and arr[i]>slg:
                slg=arr[i]
        return slg
arr = [10, 2, 8, 5]
print("Optimal approach:", solution.small(arr), solution.large(arr))