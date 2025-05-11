class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = [-i for i in nums]
        heapq.heapify(n)
        for i in range(k-1):
            heapq.heappop(n)
        
        return -n[0]
