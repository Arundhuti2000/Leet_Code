class Solution:

    def possibleStringCount(self, word: str) -> int:
        i=0
        n=len(word)
        count=1
        if n== 0:
            return 0
        while i < n:
            j=i
            while j<n and word[j]==word[i]:
                j+=1
            blocklength=j-i
            if blocklength>1:
                count+=(blocklength-1)
            i=j
        return count