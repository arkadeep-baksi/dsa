from collections import deque
class Solution:
    
    def findParent(self,node : int, parent : List[int])->int:

        if parent[node] == node:
            return node

        #Path Compression
        parent[node] = self.findParent(parent[node], parent)
        return parent[node]

    def unionByRank(self, node_a : int, node_b : int, parent : List[int], rank : List[int])->(List[int],List[int]):

        par_a = self.findParent(node_a,parent)
        par_b = self.findParent(node_b,parent)

        if rank[par_a]<rank[par_b]:
            parent[par_a] = par_b
        elif rank[par_b]<rank[par_a]:
            parent[par_b] = par_a
        else:
            parent[par_a] = par_b
            rank[par_b]+=1

        return rank,parent
    
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        parent = [i for i in range(n+1)]
        rank = [1 for i in range(n+1)]
    
        
        redundant_edges,m = 0,len(connections)
        for i in range(m):
            u,v = connections[i]
            
            par_u = self.findParent(u,parent)
            par_v = self.findParent(v,parent)

            if par_u==par_v:
                redundant_edges+=1
                continue

            else:
                rank,parent = self.unionByRank(u,v,parent,rank)

        components = 0   
        for node in range(n):
            if self.findParent(node,parent) == node:
                components+=1
                
        if redundant_edges >= components-1:
            return components-1
        else:
            return -1
        
        
          
        
        


        