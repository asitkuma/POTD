#User function Template for python3
class Solution:
	def binaryNextNumber(self, s):
		str1=""
		bool=True
		j=0
		while j<len(s) and s[j]=='0':
		    j+=1
		s=s[j:]
		for i in range(len(s)-1,-1,-1):
		    if s[i]=='0' and bool:
		        bool=False
		        str1='1'+str1
		    elif s[i]=='1' and bool:
		        str1='0'+str1
		    else:
		        str1=s[i]+str1
		if not(bool):
		    return str1
		else:
		    return '1'+str1
		

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        ans = ob.binaryNextNumber(S)
        print(ans)

# } Driver Code Ends
