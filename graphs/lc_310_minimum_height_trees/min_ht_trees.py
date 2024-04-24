from typing import List
from collections import defaultdict 
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        adj = defaultdict(set)
        for e in edges:
            adj[e[0]].add(e[1])
            adj[e[1]].add(e[0])
        leaves = []
        # collect leaves
        for k,v in adj.items():
            if len(v) == 1:
                leaves.append(k)
        
        # remove leaves from outside to center
        while len(leaves) > 0:
            if n <= 2:
                return leaves
            for i in range(len(leaves)):
                f = leaves.pop(0)
                n -= 1
                child = list(adj[f])[0]
                adj[child].remove(f)
                if len(adj[child]) == 1:
                    leaves.append(child)