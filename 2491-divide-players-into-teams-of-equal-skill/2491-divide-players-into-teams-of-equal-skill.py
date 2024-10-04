class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i = 0
        j = len(skill)-1
        sum = skill[i] + skill[j]
        res = 0
        while(i<j):
            if skill[i]+skill[j] != sum:
                return -1
            res += skill[i]*skill[j]
            i += 1
            j -= 1
            
        return res