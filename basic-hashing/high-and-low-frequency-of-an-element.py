class solution:
    def frequency(self,arr):
        freq={}
        for num in arr:
            freq[num]=freq.get(num,0)+1
        maxfreq=0
        minfreq=len(arr)
        maxele=0
        minele=0
        for ele,count in freq.items():
            if count>maxfreq:
                maxfreq=count
                maxele=ele
            if count<minfreq:
                minfreq=count
                minele=ele
        print("Element with highest frequency is %d with frequency %d" % (maxele,maxfreq))
        print("Element with lowest frequency is %d with frequency %d" % (minele
,minfreq))
s=solution()        
s.frequency([1,2,3,4,5,1,2,3])
