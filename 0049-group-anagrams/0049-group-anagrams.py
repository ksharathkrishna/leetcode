class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        old_str = strs
        new_str = []
        map = {}
        for s in strs:
            new_str.append(''.join(sorted(s)))
        i = 0
        for s in new_str:
            if s in map:
                map[s].append(old_str[i])  # Just append to the existing list
            else:
                map[s] = [old_str[i]]  # Create a new list with the current value
            i+=1

        return map.values()