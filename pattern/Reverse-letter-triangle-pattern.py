class solution:
    def pattern(self,n):
        for i in range(n,0,-1):
            for j in range(i):
                print(chr(65+j),end="")
            print()
sol=solution()
sol.pattern(5)