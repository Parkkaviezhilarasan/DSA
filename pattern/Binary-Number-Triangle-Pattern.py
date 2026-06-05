class solution:
    def pattern(self,n):
        for i in range(1,n+1):
            if i%2==0:
                num=0
            else:
                num=1
            for j in range(1,i+1):
                print(num,end="")
                num=1-num
            print()
sol=solution()
sol.pattern(5)