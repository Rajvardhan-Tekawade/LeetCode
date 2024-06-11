class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        l=[]
        for i in arr2:
            for j in range(arr1.count(i)):
                l.append(i)
        k=[]
        for i in arr1:
            if i not in arr2:
                k.append(i)
        k.sort()
        l.extend(k)
        return l