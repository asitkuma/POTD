class Solution:
    def ExtractNumber(self,sentence):
        #code here
        splited_words=sentence.split(' ')
        max1=-1
        for i in splited_words:
            bool=True
            if i.isnumeric():
                for j in i:
                    if j=='9':
                        bool=False
                        break
                if bool:
                    max1=max(max1,int(i))
        return max1

#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    S = input()
    ob = Solution()
    ans = ob.ExtractNumber(S)
    print(ans)

# } Driver Code Ends
