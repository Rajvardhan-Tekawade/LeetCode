class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l=[]
        for i in range(1,n+1):
            l.append(i)
        index=0
        while len(l)>1:
            for i in range(k-1):
                index=(index+1)%len(l)
            l.pop(index)
        return l[0]