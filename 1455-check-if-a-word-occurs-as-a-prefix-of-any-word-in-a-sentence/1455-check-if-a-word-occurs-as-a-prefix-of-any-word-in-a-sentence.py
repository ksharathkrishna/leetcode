class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = " " + sentence
        searchWord = " " + searchWord
        ind = sentence.find(searchWord)
        if ind == -1:
            return -1
        c = 1
        for i in range(ind):
            if sentence[i] == " ":
                c+=1
        return c 
