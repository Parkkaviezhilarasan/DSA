import math
def count_digits(n):
    if n==0:
        return 1
    return int(math.log10(abs(n))+1)
print(count_digits(154))

class solution:
    def cd(N):
        cnt=0
        while N>0:
            cnt=cnt+1
            N=N//10
        return cnt
print(solution.cd(1544))