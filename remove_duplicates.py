class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        c=1
        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1]:
                nums[c]=nums[i+1]
                c+=1
        return c