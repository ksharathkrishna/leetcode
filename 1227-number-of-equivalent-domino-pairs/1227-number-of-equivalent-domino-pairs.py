class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        c_map =defaultdict(int)
        for d in dominoes:
            d.sort()
            c_map[tuple(d)] += 1 
        c = 0 
        for m in c_map:
            v = c_map[m]
            c += int((v*(v-1))/2)
        return c
 
        