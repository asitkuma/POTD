
from typing import List


class Solution:
    def findClosest(self, n : int, k : int, arr : List[int]) -> int:
        # code here:-  Brute.
        # use for loop and find the number
        
        diff=k
        number=100000
        i=0
        j=n-1
        while i<=j:
            mid=(i+j)//2
            if arr[mid]<=k:
                i=mid+1
            else:
                j=mid-1
        if i>=n:
            return arr[j]
        elif j<0:
            return arr[i]
        elif abs(arr[i]-k)==abs(arr[j]-k):
            return(max(arr[i],arr[j]))
        elif abs(arr[i]-k)<abs(arr[j]-k):
            return(arr[i])
        return(arr[j])



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        k = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.findClosest(n, k, arr)
        
        print(res)
        

# } Driver Code Ends
