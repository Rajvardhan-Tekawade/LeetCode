class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        b=True
        if len(s)!=len(t):
            return False
        for i in s:
            if s.count(i)!=t.count(i):
                b=False
        return b