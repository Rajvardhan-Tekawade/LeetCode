class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        t=c=abs(x)
        rev=0
        while t>0:
            d=t%10
            rev=(rev*10)+d
            t=t//10
        rev=int(rev*(x/c))
        a=-2**31
        if rev<a or rev>-a-1:
            return 0
        return int(rev)