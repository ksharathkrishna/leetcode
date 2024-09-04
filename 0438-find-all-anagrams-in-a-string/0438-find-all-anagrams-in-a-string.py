from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        sw = s[0:len(p)]
        p_count = Counter(p)
        for i in range(len(s) - len(p) + 1):
            sw = s[i:i+len(p)]
            sw_count = Counter(sw)
            if sw_count == p_count:
                res.append(i)
        return res