class Solution:
    def solution(self, nums:List[int], ans:List[int], curr:List[int], index:int):
        if index>len(nums):
            return 
        ans.append(curr[:])
        for i in range(index, len(nums)):
            curr.append(nums[i])
            self.solution(nums, ans, curr, i+1)
            curr.pop()
        return ans

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        curr=[]
        self.solution(nums, ans, curr, 0)
        return ans