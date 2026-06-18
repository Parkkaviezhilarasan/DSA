class Solution(object):
    def nextPermutation(self, arr):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(arr)
        i=n-2
        while i>=0 and arr[i] >=arr[i+1]:
            i-=1
        if i==-1:
            left=0
            right=n-1
            while left<right:
                arr[left],arr[right]=arr[right],arr[left]
                left+=1
                right-=1
            return arr
        j=n-1
        while arr[j]<=arr[i]:
            j-=1
        arr[j],arr[i]=arr[i],arr[j]
        left=i+1
        right=n-1
        while left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        return arr
sol=Solution()
print(sol.nextPermutation([1,3,2]))
