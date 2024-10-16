class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev_max = -1
        curr_sum = 0
        for n in nums:
            curr_sum += n
            if curr_sum < 0:
                curr_sum = 0
            prev_max = max(prev_max, curr_sum)
        if prev_max == 0:
            prev_max = min(prev_max, max(nums))
        
        return prev_max