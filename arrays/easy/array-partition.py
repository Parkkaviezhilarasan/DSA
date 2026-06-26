class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        return sum(nums[::2])
sol=Solution()
print(sol.arrayPairSum([1,4,3,2]))