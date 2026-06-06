class solution:
    def prime(self,n):
        cnt=0
        for i  in range(1,n+1):
            if n%i==0:
                cnt+=1
        return cnt==2
sol=solution()
print(sol.prime(11))