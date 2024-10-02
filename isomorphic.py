class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        for i in range(len(s)):
            d1[s[i]]=t[i]
            d2[t[i]]=s[i]
        test1=""
        test2=""
        for i in range(len(s)):
            test1+=str(d1[s[i]])
            test2+=str(d2[t[i]])
        if test1==t and test2==s:
            return True
        return False