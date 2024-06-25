class Solution:
    def rotateMatrix(self, k, mat):
        # code here
        spaced_array=[]
        for i in range(len(mat)):
            spaced_array.append([0]*len(mat[0]))
            
        len1=len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                spaced_array[i][(j-k)%len1]=mat[i][j]
        return spaced_array
            
#{ 
 # Driver Code Starts
import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().strip().split(" "))
        mat = []
        for i in range(n):
            mat.append(list(map(int, input().strip().split(" "))))
        ob = Solution()
        ans = ob.rotateMatrix(k, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end=" ")
            print()

# } Driver Code Ends
