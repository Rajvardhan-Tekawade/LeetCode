class Solution:
     def longestSubarray(self, nums, limit: int) -> int:
         ans=0
         i=0
         j=0
         diff=0         
         while j<len(nums):
             l=nums[i:j+1]
             l.sort()             
             diff=abs(l[len(l)-1]-l[0])
             if diff>limit:
                 i+=1
             else:
                 ans=max(len(l),ans)
                 j+=1
         return ans