class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in nums:
            j=target-i
            if j in nums:
                if(i==j and nums.index(j)==nums.index(i) and nums.count(i)==1):
                    continue
                if(nums.index(j)==nums.index(i) and nums.count(i)==2):
                    return([nums.index(i),nums.index(i,nums.index(i)+1)])
                    break
    
                return([nums.index(i),nums.index(j)])
                break