class solution:
    def num(self,n):
        if n==0:
            return  
        print(n)
        self.num(n-1)
sol=solution()  
sol.num(10)
