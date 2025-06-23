class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        ournumber= -1
        for num in nums:
            if count==0:
                ournumber=num
            if ournumber == num:
                count+=1
            else:
                count-=1
        return ournumber

