class Solution:
  def maxProfit(self, prices: list[int]) -> int:
    l=0
    r=1
    m=0
    while r<len(prices):
        if prices[r]-prices[l]>0:
            m=max(m,prices[r]-prices[l])
        else:
            l=r
        r+=1
    return m