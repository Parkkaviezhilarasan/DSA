#handles only positive elements
def longest_subarray_optimal(arr, k):
    left = 0
    total = 0
    maxi = 0

    for right in range(len(arr)):

        total += arr[right]

        while total > k:
            total -= arr[left]
            left += 1

        if total == k:
            maxi = max(maxi, right - left + 1)

    return maxi

arr = [1,2,3,1,1,1,1,4,2,3]
k = 3

print(longest_subarray_optimal(arr, k))
#handles negative elements as well
def longest_zero_sum(arr):
    prefix_sum = 0
    maxi = 0
    d = {}

    for i in range(len(arr)):

        prefix_sum += arr[i]

        if prefix_sum == 0:
            maxi = i + 1

        if prefix_sum in d:
            maxi = max(maxi, i - d[prefix_sum])
        else:
            d[prefix_sum] = i

    return maxi

arr = [15, -2, 2, -8, 1, 7, 10, 23]
print(longest_zero_sum(arr))