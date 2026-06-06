class solution:
    def gcd(self,a,b):
        for i in range(1,min(a,b)+1):
            if a%i==0 and b %i==0:
                gcd=i
        return gcd
sol=solution()
print(sol.gcd(12,15))

class solution:
    def gcd(self,a,b):
        for i in range(min(a,b),0,-1):
            if a %i==0 and b%i==0:
                return i
sol=solution()
print(sol.gcd(12,15))

class solution:
    def gcd(self,a,b):
        while a>0 and b>0:
            if a>b:
                a=a%b
            else:
                b=b%a
        if a==0:
            return b
        return a
sol=solution()  
print(sol.gcd(12,15))