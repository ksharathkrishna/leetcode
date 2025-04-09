class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        mi = min(nums)
        c = len(set(nums))
        if mi < k:
            return -1
        if mi == k:
            return c-1
        return c
