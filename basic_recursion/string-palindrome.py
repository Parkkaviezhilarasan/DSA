class Solution(object):
    def isPalindrome(self, s):
        cleaned = "".join(c.lower() for c in s if c.isalnum())
        return self.check(cleaned,0,len(cleaned)-1)
    def check(self,s,left,right):
        if left>=right:
            return True
        if s[left]!=s[right]:
            return False
        return self.check(s,left+1,right-1)
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  