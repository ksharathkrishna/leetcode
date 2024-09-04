class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        le = 0
        prev_max = 0 
        map = {}
        while (i<len(s)):
            if map.get(s[i], -1) < 0:
                map[s[i]] = i
                le = le + 1
                i = i + 1
            else:
                prev_max = max(le, prev_max)
                le = min(i - map[s[i]] - 1, le) 
                map.pop(s[i])
        return max(prev_max, le)
