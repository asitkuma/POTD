#User function template for Python

class Solution:
    def rectanglesInCircle(self,r):
        diameter=2*r
        count=0
        for i in range(1,diameter):
            for j in range(1,diameter):
                if math.sqrt((i**2+j**2))<=diameter:
                    count+=1
                else:
                    break
        return count
                    
#{ 
 # Driver Code Starts
#Initial Template for Python

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.rectanglesInCircle(N)
        print(ans)

# } Driver Code Ends
