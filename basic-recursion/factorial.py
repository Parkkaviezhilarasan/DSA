class solution:
    def factorial(self,n):
        if n==0: 
            return 1
        return n*self.factorial(n-1)
sol=solution()
print(sol.factorial(5))