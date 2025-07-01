class Solution:

    def possibleStringCount(self, word: str) -> int:
        i=0
        count=1
        if len(word)== 0:
            return 0
        while i < len(word):
            j=i
            while j<len(word) and word[j]==word[i]:
                j+=1
            blocklength=j-i
            if blocklength>1:
                count+=(blocklength-1)
            i=j
        return count