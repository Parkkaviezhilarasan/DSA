class solution:
    def armsrrong(self,n):
        ans=0
        p=len(str(n))
        org=n
        while n>0:
            rem=n%10
            ans=ans+rem**p
            n=n//10
        return ans==org
sol=solution()  
print(sol.armsrrong(153))