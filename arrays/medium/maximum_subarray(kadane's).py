class Solution(object):
    def maxSubArray(self, nums):
        current_profit=0
        max_profit=nums[0]
        for i in range(len(nums)):
            current_profit+=nums[i]
            if current_profit > max_profit:
                max_profit=current_profit
            if current_profit<0:
                current_profit=0
        return max_profit
sol = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(sol.maxSubArray(nums))