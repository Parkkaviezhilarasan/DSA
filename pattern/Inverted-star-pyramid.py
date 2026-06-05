class solution:
    def pattern (self,N):
        for i in range(N):
            for j in range(i):
                print(" ", end="")
            for j in range(2*(N-i)-1):
                print("*",end="")
            print()
sol=solution()
sol.pattern(3)
