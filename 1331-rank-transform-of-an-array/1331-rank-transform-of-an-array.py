class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return arr
        res = sorted(arr)
        print(res)
        map = {res[0]: 1}
        rank = 1
        for i in range(1,len(res)):
            if res[i-1]!=res[i]:
                rank += 1
                map[res[i]] = rank
        for i in range(len(arr)):
            res[i] = map[arr[i]]
        return res
        