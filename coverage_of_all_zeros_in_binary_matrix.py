#User function Template for python3

class Solution:
	def findCoverage(self, matrix):
		# Code here
		ans=0
		for i in range(len(matrix)):
		    for j in range(len(matrix[0])):
		        if matrix[i][j]==0:
		            if i-1>-1:
		                if matrix[i-1][j]==1:
		                    ans+=1
		            if j-1>-1:
		                if matrix[i][j-1]==1:
		                    ans+=1
		            if i+1<len(matrix):
		                if matrix[i+1][j]==1:
		                    ans+=1
		            if j+1<len(matrix[0]):
		                if matrix[i][j+1]==1:
		                    ans+=1
		return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        ob = Solution()
        ans = ob.findCoverage(matrix)
        print(ans)

# } Driver Code Ends
