class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s[::-1]
        s=s.strip()
        c=0
        
        for i in s:
            if i!=" ":
                c+=1
            if i==" ":
                break
        return c
        