
class Solution:
    #Function to find a Mother Vertex in the Graph.
    sum1=1
    def recur(self,l1,list2,adj):
        for i in list2:
            if l1[i]!=-1:
                l1[i]=-1
                Solution.sum1+=1
                self.recur(l1,adj[i],adj)
    
    def findMotherVertex(self, V, adj):
        l3=[]
        for i in range(len(adj)):
            visited=[1 for i in range(V)]
            visited[i]=-1
            self.recur(visited,adj[i],adj)
            if Solution.sum1==V:
                l3.append(i)
                
            Solution.sum1=1
        if l3:
            return l3[0]
        return -1    

TC-O(V)*(V+E)
SC-O(V)
