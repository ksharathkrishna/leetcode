class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        t_map = defaultdict(set)
        b_map = defaultdict(set)
        for i in range(len(tops)):
            t_map[tops[i]].add(i)
            b_map[bottoms[i]].add(i)
        max_len = -1
        for i in range(1,7):
            if len(t_map[i].union(b_map[i])) == len(tops):
                max_len = max(max_len, (len(tops) - max(len(t_map[i]), len(b_map[i]))))
        
        return max_len
            
