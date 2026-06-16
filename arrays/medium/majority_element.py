#brute force approach
def majority_element(arr):
    d = {}

    for num in arr:
        d[num] = d.get(num, 0) + 1

    for key in d:
        if d[key] > len(arr) // 2:
            return key

arr = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(arr))

#optimal approach
def majority_element(arr):
    count = 0
    candidate = None

    for i in range(len(arr)):

        if count == 0:
            candidate = arr[i]

        if arr[i] == candidate:
            count += 1
        else:
            count -= 1

    return candidate

arr = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(arr))