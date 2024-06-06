class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        rep=[]
        c=len(words)
        common=set(words[0])
        for i in range(c-1):
            a=set(words[i])
            b=set(words[i+1])
            common=common.intersection(a.intersection(b))
        for i in common:
            Min=words[0].count(i)
            for j in words:
                Min=min(Min,j.count(i))
            for k in range(Min):
                rep.append(i)
        return rep