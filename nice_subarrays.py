class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = sum(1 for num in nums if num & 1)
        if count < k:
            return 0
        
        res = 0
        odd_count = 0
        prefix_sum = {0: 1}
        for num in nums:
            if num & 1:
                odd_count += 1
            res += prefix_sum.get(odd_count - k, 0)
            prefix_sum[odd_count] = prefix_sum.get(odd_count, 0) + 1
        return res