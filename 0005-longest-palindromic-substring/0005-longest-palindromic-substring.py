class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        st = ""
        for i in range(len(s)):

            # Odd len
            l, r = i, i
           
            while l>=0 and r < len(s) and s[l]==s[r]:
                if r-l+1 > max_len:
                    st = s[l:r+1]
                    max_len = max(max_len, r-l+1)
                l -= 1
                r += 1

            # Even len
            l, r = i, i+1
            
            while l>=0 and r < len(s) and s[l]==s[r]:    
                if r-l+1 > max_len:
                    st = s[l:r+1]
                    max_len = max(max_len, r-l+1)
                l -= 1
                r += 1
                
        return st