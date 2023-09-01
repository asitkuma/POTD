def printCorner(root):
    
    if root==None:
        return root
    queue=[]
    queue.append(root)
    l2=[]
    while queue:
        total_elements=len(queue)
        temp=[]
        for i in range(total_elements):
            front_element=queue[0]
            queue.pop(0)
            if front_element.left!=None:
                queue.append(front_element.left)
            if front_element.right!=None:
                queue.append(front_element.right)
            temp.append(front_element.data)
        l2.append(temp)
    for i in range(len(l2)):
        if len(l2[i])==1:
            print(l2[i][0],end=" ")
        else:
            print(l2[i][0],end=" ")
            print(l2[i][-1],end=" ")

