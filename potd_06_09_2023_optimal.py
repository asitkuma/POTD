
class Solution:
    #Function to find a Mother Vertex in the Graph.
    
    def recur(self,l1,list2,adj):
        for i in list2:
            if l1[i]!=-1:
                l1[i]=-1
                self.recur(l1,adj[i],adj)
    
    def findMotherVertex(self, V, adj):
        visited=[1 for i in range(V)]
        ans=-1
        for i in range(len(adj)):
            if visited[i]==1:
                self.recur(visited,adj[i],adj)
                ans=i
        visited=[1 for i in range(V)]
        visited[ans]=-1
        self.recur(visited,adj[ans],adj)
        if sum(visited)==-V:
            return ans
        return -1
TC-O(V)+O(V+E)+O(V)
TC-O(V)
