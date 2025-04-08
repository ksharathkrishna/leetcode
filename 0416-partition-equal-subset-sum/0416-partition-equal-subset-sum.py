class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        exp_sum = int(sum(nums)/2)
        dp = [[False for _ in range(exp_sum+1)] for _ in range(len(nums)+1)]
        for i in range(1, len(dp)):
            for j in range(len(dp[0])):
                if j == 0: #zero sum always possible
                    dp[i][j]=True
                elif nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]
                else:
                    dp[i][j]= dp[i-1][j]
        
        return dp[len(nums)][exp_sum]
