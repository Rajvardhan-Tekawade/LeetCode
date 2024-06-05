class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        c=s.count(letter)
        l=0
        for i in s:
           l+=1
        return int(((c/l)*100))