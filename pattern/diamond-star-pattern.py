class solution:
    def pattern(self, N):
        for i in range(N):
            print(" "*(N-i-1),end="")
            print("*"*(2*+i+1))
        for i in range(N):
            print(" "*i,end="")
            print("*"*(2*N-(2*i+1)))
sol=solution()
sol.pattern(3)