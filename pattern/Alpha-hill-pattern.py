class solution:
    def pattern(self,n):
        for i in range(n):
            for j in range(n-i-1):
                print(" ",end="")
            for j in range(i+1):
                print(chr(65+j),end="")
            for j in range(i):
                print(chr(65+j),end="")
            print()
sol=solution()
sol.pattern(5)