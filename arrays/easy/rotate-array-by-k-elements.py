#brute force approach1
def rotate_K(arr, k):
    n=len(arr)
    arr1=arr[:k]
    arr2=arr[k:]
    return arr2+arr1, arr1+arr2

if __name__ == "__main__":
    arr=[1,2,3,4,5,6,7]
    k=2
    print("Brute Force Approach 1:")
    print(rotate_K(arr,k))

#brute force approach2
class Solution:
    def rotate(arr,k):
        n=len(arr)
        k%=n
        temp=arr[-k:]
        for i in range(n-k-1,-1,-1):
            arr[i+k]=arr[i]
        for i in range(k):
            arr[i]=temp[i]

    def leftrotate(arr,k):
        n=len(arr)
        k%=n
        temp=arr[:k]
        for i in range(k,n):
            arr[i-k]=arr[i]
        for i in range(k):
            arr[n-k+i]=temp[i]

if __name__=="__main__":
    arr=[1,2,3,4,5,6,7]
    k=2
    print("Brute Force Approach 2: Right Rotation")
    Solution.rotate(arr,k)
    print(arr)

    arr=[1,2,3,4,5,6,7]
    print("Brute Force Approach 2: Left Rotation")
    Solution.leftrotate(arr,k)
    print(arr)

#optimal solution
class Solution:
    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    def rotate(self, arr, k, direction):
        n = len(arr)
        if n == 0:
            return
        k %= n
        if k == 0:
            return
        if direction == "right":
            self.reverse(arr, 0, n - 1)
            self.reverse(arr, 0, k - 1)
            self.reverse(arr, k, n - 1)
        elif direction == "left":
            self.reverse(arr, 0, k - 1)
            self.reverse(arr, k, n - 1)
            self.reverse(arr, 0, n - 1)
        else:
            print("Invalid direction! Use 'left' or 'right'")

if __name__ == "__main__":
    sol = Solution()
    print("Optimal Solution:")
    arr1 = [1, 2, 3, 4, 5, 6, 7]
    sol.rotate(arr1, 2, "right")
    print("Right Rotation:", arr1)

    arr2 = [1, 2, 3, 4, 5, 6, 7]
    sol.rotate(arr2, 2, "left")
    print("Left Rotation :", arr2)