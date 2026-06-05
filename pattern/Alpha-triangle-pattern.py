class solution:
    def pattern(self,n):
        for i in range(n):
            for j in range(n-1-i,n):
                print(chr(65+j),end="")
            print()
sol=solution()
sol.pattern(5)