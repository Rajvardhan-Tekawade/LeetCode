class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        c=d=0
        for i in candyType:
            c+=1
        candyType=set(candyType)
        
        for i in candyType:
            d+=1
        if d>c//2:
            return c//2
        else:
            return d