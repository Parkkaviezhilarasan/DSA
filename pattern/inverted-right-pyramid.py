class solution:
    def pattern(self,N):
        for i in range(N):
            print("*"*N)
            N=N-1
sol=solution()
sol.pattern(3)