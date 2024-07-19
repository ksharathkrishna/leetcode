class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r= 1, n
        ans = -1
        while(l<=r):
            m = (l+r)//2
            if (m*(m+1))<=2*n:
                l = m+1
                ans = m
            else:
                r = m-1
        return ans