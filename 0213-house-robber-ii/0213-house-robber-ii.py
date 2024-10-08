class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        s1 = self.helper(nums[1:])
        s2 = self.helper(nums[:len(nums)-1])
        return max(s1, s2)
    def helper(self, nums) -> int:
        r1, r2 = 0, 0
        for n in nums:
            t = max(n+ r1, r2)
            r1 = r2
            r2 = t
        return r2