class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        q = [ (-1)*n for n in nums]
        sc = 0
        heapq.heapify(q)
        while k:
            max_val = (-1) * heapq.heappop(q)
            sc += max_val
            max_val = math.ceil(max_val/3)
            heapq.heappush(q, (-1) * max_val)
            k -= 1
        return sc