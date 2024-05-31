
class Solution:
    def recur(self,str1,str2,map1,i,j):
        if j<0:
            return 1
        if i<0:
            return 0
        if (i,j) in map1:
            return map1[(i,j)]
        if str1[i]==str2[j]:
            one=self.recur(str1,str2,map1,i-1,j-1)
            two=self.recur(str1,str2,map1,i-1,j)
            map1[(i,j)]=(one+two)%(10**9+7)
            return map1[(i,j)]
        else:
            return self.recur(str1,str2,map1,i-1,j)
    def countWays(self, str1 : str, s2 : str) -> int:
        # code here
        new_str=""
        for i in str1:
            if i in s2:
                new_str+=i
        map1={}
        return self.recur(new_str,s2,map1,len(new_str)-1,len(s2)-1)
        
        


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s1 = (input())

        s2 = (input())

        obj = Solution()
        res = obj.countWays(s1, s2)

        print(res)

# } Driver Code Ends
