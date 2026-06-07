class solution:
    def num(self,i,n):
        if i >n:
            return 
        print(i)
        self.num(i+1,n)
sol=solution()
sol.num(1,10)