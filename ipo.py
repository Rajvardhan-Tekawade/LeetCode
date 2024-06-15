class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        current=w
        q=collections.deque(sorted(zip(profits,capital), key=lambda x:(x[1],-x[0])))
        h=[]
        for _ in range(k):
            while len(q)>0 and q[0][1]<=current:
                p, _=q.popleft()
                heapq.heappush(h,-p)
            if len(h)==0:
                break
            p=-heapq.heappop(h)
            current+=p
        return current