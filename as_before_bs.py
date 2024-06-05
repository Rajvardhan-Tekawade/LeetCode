class Solution:
    def checkString(self, s: str) -> bool:
        s=s[::-1]
        if 'a' in s:
            i=s.index('a')
            if 'b' not in s[i:]:
                return True
        else:
            return True
        return False
        