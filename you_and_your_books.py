
class Solution:
    #Your task is to complete this function
    #Function should return an integer
    #a - list/array containing height of stack's respectively
    def max_Books(self, n, k, arr):
        i=0
        maxi=0
        while i<len(arr):
            if arr[i]<=k:
                j=i
                temp=0
                while j<len(arr) and arr[j]<=k:
                    temp+=arr[j]
                    j+=1
                maxi=max(maxi,temp)
                i=j
            else:
                i+=1
        return maxi
        


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        temp = list(map(int, input().strip().split()))
        n = temp[0]
        k = temp[1]
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.max_Books(n, k, arr))
# Contributed by:Harshit Sidhwa

# } Driver Code Ends
