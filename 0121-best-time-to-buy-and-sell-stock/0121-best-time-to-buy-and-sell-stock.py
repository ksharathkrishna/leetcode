class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev_min = math.inf
        profit = 0
        for p in prices:
            if p > prev_min:
                profit = max( p- prev_min, profit)
            else:
                prev_min = p
        return profit
                