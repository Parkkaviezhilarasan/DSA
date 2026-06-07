class solution:
    def reverse(self, arr, i):
        n=len(arr)
        if i >=n//2:
            return 
        arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
        self.reverse(arr,i+1)
sol=solution()
arr=[1,2,3,4,5]
sol.reverse(arr,0)
print(arr)