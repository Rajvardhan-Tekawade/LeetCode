class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        for i in range(len(edges)-1):
            for j in edges[i]:
                if j in edges[i+1]:
                    center=j
        return center