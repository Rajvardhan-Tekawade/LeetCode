class Solution:
    def removeElement(self, nums , val: int) -> int:
        for i in range(nums.count(val)):
            nums.remove(val)
        return len(nums)