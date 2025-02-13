class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        no_of_op = 0
        while True:
            x = heapq.heappop(nums)
            if x>=k:
                break
            y = heapq.heappop(nums)
            heapq.heappush(nums, 2*x + y)
            no_of_op += 1
        return no_of_op
        