class Solution(object):
    def subarraySum(self, nums, k):

        prefixSum = 0
        count = 0
        mp = {0: 1}

        for num in nums:

            prefixSum += num

            if (prefixSum - k) in mp:
                count += mp[prefixSum - k]

            if prefixSum in mp:
                mp[prefixSum] += 1
            else:
                mp[prefixSum] = 1

        return count


sol = Solution()
nums = [1,1,1]
k = 2

print(sol.subarraySum(nums, k))