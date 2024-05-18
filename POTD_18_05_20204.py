#User function Template for python3
from typing import List

class Solution:
	def findPeakElement(self, arr):
	    
	    #Bruteforce.
	    return max(arr)  #ha ha :-----> Time complexity:-O(n)
	    
		i=0
		j=len(arr)-1
		while i<j:
		    mid=(i+j)//2
		    if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
		        return arr[mid]
		    elif arr[mid]<arr[mid+1]:
		        i=mid+1
		    else:
		        j=mid-1
		return arr[i]  #Time complexity:-   O(logn)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        ob = Solution()
        ans = ob.findPeakElement(a)
        print(ans)

# } Driver Code Ends
