
class Solution:
    def oddEven(self, s : str) -> str:
        
        #Bruteforce.. here tc:-o(n) and sc:-we cant say that it would be n but near about n.
        
        # map1={}
        # for i in s:
        #     if i not in map1:
        #         map1[i]=0
        #     map1[i]+=1
        # count=0
        # for i,j in map1.items():
        #     if (ord(i)%2==1 and j%2==1) or (ord(i)%2==0 and j%2==0):
        #         count+=1
        # return 'ODD' if count%2 else "EVEN"
        
        #smart way of doing.You know that total 26 space will be required o(n) and o(1)
        
        # l1=[0]*26
        # for i in s:
        #     l1[ord(i)-97]+=1
        # count=0
        # for i in s:
        #     if ((ord(i)%2==1 and l1[ord(i)-97]%2==1) or (ord(i)%2==0 and l1[ord(i)-97]%2==0)) and l1[ord(i)-97]!=-1:
        #         l1[ord(i)-97]=-1
        #         count+=1
        # return 'ODD' if count%2 else "EVEN"


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s = (input())

        obj = Solution()
        res = obj.oddEven(s)

        print(res)

# } Driver Code Ends
