class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def generateAllBinaryStrings(n, arr): 
            for i in range(1 << n):
                # Convert the current number to a binary string of length n
                binary_str = format(i, '0' + str(n) + 'b') 
                arr.append(binary_str)
        res = ""
        n = len(nums)
        arr = list()
        map = {}
        generateAllBinaryStrings(n, arr) 
        for s in nums:
            map[s] = 1
        for s in arr:
            if not map.get(s):
                res = s
                break
        return res

        