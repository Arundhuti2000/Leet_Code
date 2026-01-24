class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for char in s:
            if (char.isalpha() or char.isnumeric()):
                string+=char
        newstring=string.lower()
        left=0
        right= len(newstring)-1
        while left <right:
            if newstring[left]== newstring[right]:
                left+=1
                right-=1
            else:
                return False
        return True