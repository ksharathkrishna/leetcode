class Solution:
    def climbStairs(self, n: int) -> int:
        f, s = 1, 1
        for i in range(2, n+1):
            t = f + s
            f = s
            s = t
        
        return s