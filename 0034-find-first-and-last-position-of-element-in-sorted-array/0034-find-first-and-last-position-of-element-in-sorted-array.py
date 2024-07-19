class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r= 0, len(nums)-1
        while(l<=r):
            m = (l+r)//2
            print(m)
            if nums[m] == target:
                l = r = m
                while True:
                    if l-1>=0 and nums[l-1] == nums[m]: l-=1
                    elif r+1<len(nums) and nums[r+1] == nums [m]: r+=1
                    else:
                        return[l, r]
            elif nums[m] < target:
                l=m+1
            else:
                r=m-1
        return [-1,-1]