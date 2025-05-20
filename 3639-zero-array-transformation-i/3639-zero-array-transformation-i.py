class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        freq = defaultdict(int)
        for l, r in queries:
            freq[l] += 1
            freq[r + 1] -= 1

        for i in range(1, len(nums)):
            freq[i] += freq[i - 1]

        for n in range(len(nums)):
            if freq[n] < nums[n]:
                return False
        return True 