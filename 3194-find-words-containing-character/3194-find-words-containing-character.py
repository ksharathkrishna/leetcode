class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i in range(len(words)):
            s = set(words[i])
            if x in s:
                res.append(i)
        return res