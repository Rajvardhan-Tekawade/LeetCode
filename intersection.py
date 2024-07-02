class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        for i in nums1:
            if i in nums2:
                l.append(i)
        l=set(l)
        c=[]
        for i in l:
            for j in range(min(nums1.count(i),nums2.count(i))):
                c.append(i)
        return c