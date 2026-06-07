class solution:
    def name(self,name,n):
        if n==0:
            return 
        print(name)
        self.name(name,n-1)
sol=solution()
sol.name("sachin",5)