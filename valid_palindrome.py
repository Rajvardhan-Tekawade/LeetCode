class Solution:
    def isPalindrome(self, s: str) -> bool:
        r=""
        for _ in s:
            if _.isalnum()==True:
                r=r+_    
        r=r.lower()
        if r[::-1]==r:
            return True
        return False