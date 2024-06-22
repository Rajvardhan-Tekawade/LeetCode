class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for _ in nums:
            if nums.count(_)>len(nums)//2:
                return _