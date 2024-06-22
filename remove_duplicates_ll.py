class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c=set(nums)
        for _ in c:
            if nums.count(_)>2:
                while nums.count(_)>2:
                    nums.remove(_)
        return len(nums)