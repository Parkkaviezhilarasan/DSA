class solution:
    def pattern (self,N):
        for i in range(1,N+1):
            for j in range(1,i+1):
                print(i,end="")
            print()
sol=solution()
sol.pattern(3)