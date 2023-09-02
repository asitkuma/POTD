#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''
class Solution:
    def getCount(self,root,n):
        #code here
        queue=[root]
        l2=[]
        index=1
        while queue:
            size=len(queue)
            for i in range(size):
                element=queue[0]
                if element.left!=None:
                    queue.append(element.left)
                if element.right!=None:
                    queue.append(element.right)
                if element.left==None and element.right==None:
                    l2.append(index)
                queue.pop(0)
            index+=1
        sum1=0
        count=0
        for i in range(len(l2)):
            sum1+=l2[i]
            if sum1>n:
                break
            count+=1
        return count
        
        