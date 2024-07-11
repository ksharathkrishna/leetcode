class Solution:
    def candy(self, ratings: List[int]) -> int:
        l = [1] * len(ratings)
        r = [1] * len(ratings)
        s = 0
        i = 1
        j = len(ratings) - 2
        # left to right
        while i < len(ratings):
            if ratings[i]>ratings[i-1]: 
                l[i] = l[i-1] + 1
            i += 1
        # right to left
        while j >=0 :
            if ratings[j]>ratings[j+1]: 
                r[j] = r[j+1] + 1
            j -= 1
        # calc max from 2 sub problems
        for i in range(len(ratings)):
            s += (max(l[i],r[i]))
        return s 
