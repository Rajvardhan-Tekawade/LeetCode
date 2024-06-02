class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits=digits[::-1]
        d=0
        for i in digits:
            d+=1

        if d==digits.count(9):
            digits=[1]
            for i in range(d):
                digits.append(0)
            return digits
            
        c=0
        sum=digits[0]=digits[0]+1
        while sum==10:
            digits[c]=0
            sum=digits[c+1]=digits[c+1]+1
            c+=1
        digits=digits[::-1]
        return digits