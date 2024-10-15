class Solution:
    def minimumSteps(self, s: str) -> int:
        swaps = 0 
        count_1 = 0
        for c in s:
            if c == '1':
                count_1 += 1
            else:
                swaps += count_1
        return swaps