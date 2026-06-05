class solution:
    def pattern(self, N):
        for i in range(1,N+1):
            print("*"*i)
        for i in range(N,0,-1):
            print("*"*i)
sol=solution()
sol.pattern(3)