class solution:
    def reverse(self,n):
        rev=0
        sign=1 if n>0 else -1
        n=abs(n)
        while n>0:
            rem=n%10
            rev=rev*10+rem
            n=n//10
        if rev<-2**31 or rev > 2**31-1:
            return 0
        return rev *sign
sol=solution()
print(sol.reverse(-1234))