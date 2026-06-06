class solution:
    def palindrome(self,n):
        rev=0
        org=n
        if n < 0 or (n%10==0 and n!=0):
            return False
        while n>0:
            rem=n%10
            rev=rev*10+rem
            n=n//10
        return rev==org
sol=solution()  
print(sol.palindrome(12321))

class solution:
    def palindrome(self,n):
        if n<0 or (n%10==0 and n!=0):
            return False
        rev=0
        while n>rev:
            rem=n%10
            rev=rev*10+rem
            n=n//10
        return n==rev or n==rev//10
sol=solution()  
print(sol.palindrome(12321))
