class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        max_lis = 0

        # max length starting from index i
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i]<nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
            max_lis = max(max_lis, LIS[i])

        return max_lis