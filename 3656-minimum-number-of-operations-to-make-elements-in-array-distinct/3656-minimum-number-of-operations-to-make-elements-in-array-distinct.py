class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c = 0
        while len(nums)>0:
            if len(set(nums)) == len(nums):
                return c
            n = 3 if len(nums)>3 else len(nums)
            nums = nums[n:]
            c += 1 
        return c