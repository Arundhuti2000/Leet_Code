class Solution:
    def findLHS(self, nums: List[int]) -> int:
        maxLen=0
        count={}
        for num in nums:
            count[num]=count.get(num,0)+1
        for num in count:
            if (num+1) in count:
                maxLen = max(maxLen, count[num] + count[num+1])
        return maxLen