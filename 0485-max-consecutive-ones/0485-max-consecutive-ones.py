class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcnt=0
        cnt=0
        for num in nums:
            if num==1:
                cnt+=1
                maxcnt = max(maxcnt,cnt)
            elif num == 0:
                cnt=0
        return maxcnt