#User function Template for python3

class Solution:
    def pattern (self, arr):
        # code here
        str_Var=""
        if len(arr)==1:
            return '0 R'
        for i in range(len(arr)):
            str1=""
            for j in range(len(arr[0])):
                str1+=str(arr[i][j])
            if str1==str1[::-1]:
                dummy=""
                dummy=str(i)+" "+'R'
                return dummy
                
                
        for i in range(len(arr)):
            str1=""
            for j in range(len(arr[0])):
                str1+=str(arr[j][i])
            if str1==str1[::-1]:
                dummy=""
                dummy=str(i)+" "+'C'
                return dummy
        return -1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        a = list()
        c = 0
        for i in range(0, n):
            X = list()
            for j in range(0, n):
                X.append(arr[c])
                c += 1
            a.append(X)
        ans = ob.pattern(a)
        print(ans)

# } Driver Code Ends
