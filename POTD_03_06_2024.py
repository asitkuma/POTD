
#Bruteforce....
class Solution:
    def numberOfConsecutiveOnes (ob,n):
        first=0
        second=1
        l1=[0]*(n-1)
        l1[0]=1
        for i in range(3,n+1):
            ans=(first+second)%(10**9+7)
            l1[i-2]=((l1[i-3]*2)+ans)%(10**9+7)
            first=second
            second=ans
        return l1[-1]

#optimal..
def recur(n):
    if n==2:
        return 1,0,1
    ans=recur(n-1)
    return (ans[0]*2+(ans[1]+ans[2]))%(10**9+7),ans[2],(ans[2]+ans[1])%(10**9+7)
