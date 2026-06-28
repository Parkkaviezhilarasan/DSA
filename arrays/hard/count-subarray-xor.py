def countsubxor(arr,k):
    freq={0:1}
    prefix_xor=0
    count=0
    for num in arr:
        prefix_xor^=num
        count+=freq.get(prefix_xor^k,0)
        freq[prefix_xor]=freq.get(prefix_xor,0)+1   
        
    return count    
arr=[4,2,2,6,4]
k=6
print(countsubxor(arr,k))