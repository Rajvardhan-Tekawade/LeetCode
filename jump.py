class Solution:
    def canJump(self, nums) -> bool:
        i=k=0
        while i<len(nums):
            k=nums[i]
            i+=k
        if(k==len(nums)-1):
            return True
        return False