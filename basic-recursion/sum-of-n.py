class solution:
    def sum_num(self,n):
        if n==0:
            return 0
        return n+self.sum_num(n-1)
sol=solution()
print(sol.sum_num(5))