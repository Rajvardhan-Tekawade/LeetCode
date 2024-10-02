class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr)==0:
            return []
        if arr.count(arr[0])==len(arr):
            for i in range (len(arr)):
                arr[i]=1
            return arr
        a=arr[:]
        a.sort()
        d={}
        c=1
        for i in a:
            if i not in d.keys():
                d[i]=c
                c+=1
        l=[]
        for i in arr:
            l.append(d[i])
        return l