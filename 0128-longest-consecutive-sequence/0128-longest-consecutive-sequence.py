class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums = list(set(nums))
        nums.sort()
        res = 1
        max_res = 0
        
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] == 1:
                res+=1
            else:
                max_res = max(max_res, res)
                res = 1
            
        return max(max_res, res)