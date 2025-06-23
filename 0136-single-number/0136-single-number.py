class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen=set(nums)
        n=len(nums)
        return 2*(sum(seen))-sum(nums)
        return 0