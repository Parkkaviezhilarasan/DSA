class Solution(object):
    def findMaxConsecutiveOnes(self, arr):
        count = 0
        maxi = 0
        for i in range(len(arr)):
            if arr[i] == 1:
                count += 1
            else:
                count = 0
            maxi = max(count, maxi)
        return maxi
sol = Solution()
arr = [1,1,0,1,1,1]
print(sol.findMaxConsecutiveOnes(arr))