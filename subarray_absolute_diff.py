from collections import deque

class Solution:
    def longestSubarray(self, nums, limit: int) -> int:
        ans = 0
        i = 0
        max_deque = deque()
        min_deque = deque()
        
        for j in range(len(nums)):
            while max_deque and max_deque[-1] < nums[j]:
                max_deque.pop()
            max_deque.append(nums[j])
            
            while min_deque and min_deque[-1] > nums[j]:
                min_deque.pop()
            min_deque.append(nums[j])
            
            while max_deque[0] - min_deque[0] > limit:
                if max_deque[0] == nums[i]:
                    max_deque.popleft()
                if min_deque[0] == nums[i]:
                    min_deque.popleft()
                i += 1
            
            ans = max(ans, j - i + 1)
        
        return ans