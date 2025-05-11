class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        if len(nums) >= k:
            n =nums[len(nums)-k:]
            heapify(n) 
            self.h = n
        else:
            heapify(nums) 
            self.h = nums
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        if len(self.h) > self.k:
            heapq.heappop(self.h)
        return self.h[0] if self.h else None
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)