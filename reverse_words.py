class Solution:
    def reverseWords(self, s: str) -> str:
        
        t=s.split(" ")
        s=""
        for i in t[::-1]:
            if i!="":
                s=s+" "+i
        return s[1:]