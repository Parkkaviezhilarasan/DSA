class solution:
    def frequency(self,arr,q):
        hash_arr=[0]*100001
        for num in arr:
            hash_arr[num]+=1
        for x in q:
            print(hash_arr[x])
s=solution()
s.frequency([1,2,3,4,5,1,2,3],[1,2,3,4,5,6])

class solution:
    def frequency(self,arr,q):
        freq={}
        for num in arr:
            freq[num]=freq.get(num,0)+1
        for x in q:
            print("Frequency of %d is %d" % (x, freq.get(x,0)))
s=solution()
s.frequency([1,2,3,4,5,1,2,3],[1,2,3,4,5,6])