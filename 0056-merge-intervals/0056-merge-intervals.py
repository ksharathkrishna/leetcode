class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals, key=lambda x: x[0])
        prev_int = [intervals[0][0], intervals[0][1]]
        for i in range(1, len(intervals)):
            if prev_int[1] < intervals[i][0]:
                res.append(prev_int)
                prev_int = intervals[i]
            else:
                prev_int = [min(prev_int[0], intervals[i][0]), max(prev_int[1], intervals[i][1])]
        res.append(prev_int)
        return res        