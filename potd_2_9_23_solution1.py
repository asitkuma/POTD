def recur(root,l1,index=1):
    if root==None:
        return
    if root.left==None and root.right==None:
        l1.append(index)
        return
    index+=1
    recur(root.left,l1,index)
    recur(root.right,l1,index)
    index-=1

class Solution:
    def getCount(self,root,n):
        #code here
        l1=[]
        sum1=0
        count=0
        recur(root,l1)
        l1.sort()
        for i in l1:
            sum1+=i
            if sum1>n:
                break
            count+=1
        return count
