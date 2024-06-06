class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        c=s.count(letter)
        l=len(s)
        return int(((c/l)*100))