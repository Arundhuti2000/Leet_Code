class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        result = []
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in seen:
                result.append(seen[compliment])
                result.append(i)
            else:
                seen[nums[i]]= i
        return result