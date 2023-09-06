class Solution:
    def printGraph(self, V : int, edges : List[List[int]]) -> List[List[int]]:
        # code here
        vertices=[[] for _ in range(V)]
        
        for i in edges:
            vertices[i[0]].append(i[1])
            vertices[i[1]].append(i[0])
        return vertices

TC-O(E)*O(1)
Sc:-O(V)
