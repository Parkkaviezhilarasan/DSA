class solution:
    def divisor(self,n):
        res=[]
        for i in range(1,n+1):
            if n%i==0:
                res.append(i)
        return res
sol=solution()  
print(sol.divisor(12))

import math
class solution:
    def divisor(self,n):
        res=[]
        for i in range(1,int(math.sqrt(n))+1):
            if n%i==0:
                res.append(i)
                if i !=  n//i:
                    res.append(n//i)
        res.sort()
        return res  
sol=solution()  
print(sol.divisor(12))