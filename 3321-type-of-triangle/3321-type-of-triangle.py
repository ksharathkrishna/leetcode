class Solution:
    def triangleType(self, nums: List[int]) -> str:
        ts = set(nums)
        if len(ts) == 1: return "equilateral"
        else:
            t = True
            for i in range(3):
                t = t and nums[i]<nums[(i+1)%3]+nums[(i+2)%3]
            if not t: return "none"
            if len(ts) == 2: return "isosceles"
            else: return "scalene"
        return "none"
        