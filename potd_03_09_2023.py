class Solution:
    # Return True if the given trees are isomotphic. Else return False.
    def recur(self,root1,l1,l3):
        if root1==None:
            return
        if root1.left!=None:
            l1.append(root1.left.data)
        if root1.right!=None:
            l1.append(root1.right.data)
        l3.append((root1.data,sum(l1.copy())))
        l1.clear()
        self.recur(root1.left,l1,l3)
        self.recur(root1.right,l1,l3)
        
    
    def isIsomorphic(self, root1, root2): 
        #code here.
        l1=[]
        l2=[]
        l3=[]
        l4=[]
        self.recur(root1,l1,l3)
        self.recur(root2,l2,l4)
        d1={}
        d2={}
        for i in l3:
            if i not in d1:
                d1[i]=0
            d1[i]+=1
        for i in l4:
            if i not in d2:
                d2[i]=0
            d2[i]+=1
        return d1==d2
        
        
