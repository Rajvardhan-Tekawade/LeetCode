class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        index=0
        c=0
        sm=len(strs[0])
        for a in range(len(strs)):
            sm=min(sm,len(strs[a]))
        while index<sm:
            s=strs[0][index]
            for i in strs:
                if s!=i[index]:
                    c=1
                    break
            if c==1:
                break
            index+=1
        s=strs[0][:index]
        return s