class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern)>1 and s.count(" ")==0:
            return False
        d1={}
        d2={}
        l1=[]
        l2=[]
        s+=" "
        word=""
        for i in pattern:
            l1.append(i)
        for j in s:
            if j==" ":
                l2.append(word)
                word=""
            else:
                word+=j
        s=s[:-1]
        for i in range(len(l1)):
                d1[l1[i]]=l2[i]
                d2[l2[i]]=l1[i]
                
        text1=[]
        text2=[]
        for i in range(len(pattern)):
            text1.append(d1[l1[i]])
            text2.append(d2[l2[i]])
        if text1==l2 and text2==l1:
            return True
        return False