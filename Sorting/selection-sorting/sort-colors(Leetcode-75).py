class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        for i in range(n-1):
            min_ele=i
            for j in range(i+1,n):
                if nums[j]<nums[min_ele]:
                    min_ele=j
            nums[i],nums[min_ele]=nums[min_ele],nums[i]
        return nums
s=Solution()
print(s.sortColors([2,0,2,1,1,0]))