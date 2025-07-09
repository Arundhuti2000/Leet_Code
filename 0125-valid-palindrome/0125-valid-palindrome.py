class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s = ''.join(filter(str.isalnum, s))
        
        print(s)
        for i in range(0,len(s)):
            if s[-i-1] != s[i]:
                print(s[-i],s[i])
                return False
        return True