class Solution:
    def getLucky(self, s: str, k: int) -> int:
        sum = ''
        for c in s:
            sum+=str(((ord(c)-ord('a'))+1))
        sum = int(sum)

        while k > 0:
            new_sum = 0
            for digit in str(sum):  
              new_sum += int(digit)  
            sum = new_sum 
            k-=1
        return sum