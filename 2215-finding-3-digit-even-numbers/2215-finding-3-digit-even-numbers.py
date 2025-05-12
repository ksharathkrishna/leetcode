class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res =set()
        for i,h in enumerate(digits):
            if h == 0: continue
            for j, t in   enumerate(digits):
                for k, o in  enumerate(digits):
                    if i==j or j==k or k==i or o%2 == 1: continue
                    res.add(h*100+t*10+o)
        return sorted(list(res))
        