#User function Template for python3

class Solution:
    def printKClosest(self, arr, n, k, x):
        # code here
        i=0
        j=n-1
        is_there=False
        temp_list=[]
        while i<=j:
            mid=(i+j)//2
            if arr[mid]==x:
                is_there=True
            if arr[mid]>x:
                j=mid-1
            else:
                i=mid+1
        if is_there:
            j-=1
            
        while k!=0:
            if i<n and abs(arr[i]-x)<=abs(arr[j]-x):
                temp_list.append(arr[i])
                i+=1
            else:
                temp_list.append(arr[j])
                j-=1
            k-=1
        return temp_list




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k, x = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.printKClosest(arr, n, k, x)
        for xx in ans:
            print(xx, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
