class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0]*len(height)
        right = [0]*len(height)
        lmax, rmax, water = 0, 0, 0
        
        # left max
        for i in range(len(height)):
            lmax = max(lmax, height[i])
            left[i] = lmax
        
        # right max
        for i in range(len(height) - 1, -1, -1):
            rmax = max(rmax, height[i])
            right[i] = rmax
        
        print(left, right)
        # total capacity
        for i in range(len(height)):
            water += min(left[i], right[i]) - height[i]
        
        return water