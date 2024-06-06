class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        c=len(candyType)
        candyType=set(candyType)
        len(candyType)
        if len(candyType)>c//2:
            return c//2
        else:
            return len(candyType)